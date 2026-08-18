#!/usr/bin/env python3
"""NetControl: dependency-free network diagnostics and monitoring CLI."""

from __future__ import annotations

import argparse
import ipaddress
import json
import logging
import platform
import shutil
import socket
import struct
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python < 3.11
    tomllib = None

VERSION = "1.0.0"
LOG = logging.getLogger("netcontrol")
TCP_STATES = {
    "01": "ESTABLISHED", "02": "SYN_SENT", "03": "SYN_RECV",
    "04": "FIN_WAIT1", "05": "FIN_WAIT2", "06": "TIME_WAIT",
    "07": "CLOSE", "08": "CLOSE_WAIT", "09": "LAST_ACK",
    "0A": "LISTEN", "0B": "CLOSING",
}


@dataclass
class InterfaceStats:
    name: str
    state: str
    mtu: int | None
    mac: str | None
    rx_bytes: int
    tx_bytes: int
    rx_packets: int
    tx_packets: int
    rx_errors: int
    tx_errors: int


def _read(path: Path, default: str = "") -> str:
    try:
        return path.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError):
        return default


def _integer(path: Path) -> int | None:
    value = _read(path)
    try:
        return int(value)
    except ValueError:
        return None


def interfaces(proc_net_dev: Path = Path("/proc/net/dev"), sys_class: Path = Path("/sys/class/net")) -> list[InterfaceStats]:
    """Read interface counters without invoking external programs."""
    result: list[InterfaceStats] = []
    lines = _read(proc_net_dev).splitlines()[2:]
    for line in lines:
        if ":" not in line:
            continue
        name, values = line.split(":", 1)
        name, fields = name.strip(), values.split()
        if len(fields) < 16:
            continue
        base = sys_class / name
        result.append(InterfaceStats(
            name=name,
            state=_read(base / "operstate", "unknown"),
            mtu=_integer(base / "mtu"),
            mac=_read(base / "address") or None,
            rx_bytes=int(fields[0]), tx_bytes=int(fields[8]),
            rx_packets=int(fields[1]), tx_packets=int(fields[9]),
            rx_errors=int(fields[2]), tx_errors=int(fields[10]),
        ))
    return sorted(result, key=lambda item: item.name)


def _decode_ipv4(raw: str) -> str:
    return socket.inet_ntoa(struct.pack("<I", int(raw, 16)))


def routes(path: Path = Path("/proc/net/route")) -> list[dict[str, Any]]:
    result = []
    for line in _read(path).splitlines()[1:]:
        fields = line.split()
        if len(fields) < 11:
            continue
        try:
            mask = _decode_ipv4(fields[7])
            prefix = ipaddress.IPv4Network(f"0.0.0.0/{mask}").prefixlen
            destination = f"{_decode_ipv4(fields[1])}/{prefix}"
            result.append({"interface": fields[0], "destination": destination,
                           "gateway": _decode_ipv4(fields[2]), "metric": int(fields[6])})
        except (ValueError, OSError):
            continue
    return result


def _endpoint(raw: str, ipv6: bool) -> str:
    address, port = raw.split(":")
    packed = bytes.fromhex(address)
    if ipv6:
        # Linux stores each 32-bit word in host byte order.
        packed = b"".join(packed[i:i + 4][::-1] for i in range(0, 16, 4))
        host = socket.inet_ntop(socket.AF_INET6, packed)
        return f"[{host}]:{int(port, 16)}"
    return f"{socket.inet_ntoa(packed[::-1])}:{int(port, 16)}"


def connections(proc_net: Path = Path("/proc/net"), listening_only: bool = False) -> list[dict[str, Any]]:
    result = []
    for protocol in ("tcp", "tcp6", "udp", "udp6"):
        for line in _read(proc_net / protocol).splitlines()[1:]:
            fields = line.split()
            if len(fields) < 10:
                continue
            state = TCP_STATES.get(fields[3], fields[3]) if protocol.startswith("tcp") else "UNCONN"
            if listening_only and state != "LISTEN":
                continue
            try:
                result.append({"protocol": protocol, "local": _endpoint(fields[1], protocol.endswith("6")),
                               "remote": _endpoint(fields[2], protocol.endswith("6")),
                               "state": state, "uid": int(fields[7]), "inode": int(fields[9])})
            except (ValueError, OSError):
                continue
    return result


def dns_lookup(host: str) -> list[dict[str, str]]:
    answers = set()
    for family, socktype, _proto, _canon, sockaddr in socket.getaddrinfo(host, None):
        answers.add(("IPv6" if family == socket.AF_INET6 else "IPv4", sockaddr[0],
                     "TCP" if socktype == socket.SOCK_STREAM else "UDP"))
    return [{"family": family, "address": address, "transport": transport}
            for family, address, transport in sorted(answers)]


def tcp_check(host: str, port: int, timeout: float) -> dict[str, Any]:
    started = time.monotonic()
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return {"host": host, "port": port, "reachable": True,
                    "latency_ms": round((time.monotonic() - started) * 1000, 2), "error": None}
    except OSError as exc:
        return {"host": host, "port": port, "reachable": False,
                "latency_ms": round((time.monotonic() - started) * 1000, 2), "error": str(exc)}


def ping(host: str, count: int, timeout: float) -> dict[str, Any]:
    executable = shutil.which("ping")
    if not executable:
        raise RuntimeError("'ping' wurde nicht gefunden")
    flag = "-n" if platform.system() == "Windows" else "-c"
    timeout_args = ["-w", str(max(1, int(timeout * 1000)))] if platform.system() == "Windows" else ["-W", str(max(1, int(timeout)))]
    command = [executable, flag, str(count), *timeout_args, host]
    completed = subprocess.run(command, capture_output=True, text=True, timeout=(count * timeout) + 5, check=False)
    return {"host": host, "reachable": completed.returncode == 0, "returncode": completed.returncode,
            "output": (completed.stdout or completed.stderr).strip()}


def snapshot() -> dict[str, Any]:
    hostname = socket.gethostname()
    return {"timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "hostname": hostname, "addresses": dns_lookup(hostname),
            "interfaces": [asdict(item) for item in interfaces()], "routes": routes(),
            "connection_summary": _connection_summary(connections())}


def _connection_summary(items: list[dict[str, Any]]) -> dict[str, int]:
    summary: dict[str, int] = {}
    for item in items:
        key = f"{item['protocol']}:{item['state']}"
        summary[key] = summary.get(key, 0) + 1
    return summary


def load_config(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    if tomllib is None:
        raise RuntimeError("TOML-Konfiguration benötigt Python 3.11+")
    with open(path, "rb") as handle:
        return tomllib.load(handle)


def render(data: Any, json_output: bool) -> None:
    if json_output:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    if isinstance(data, list):
        if not data:
            print("Keine Einträge.")
            return
        columns = list(data[0]) if isinstance(data[0], dict) else []
        widths = {key: max(len(key), *(len(str(row.get(key, ""))) for row in data)) for key in columns}
        print("  ".join(key.upper().ljust(widths[key]) for key in columns))
        print("  ".join("-" * widths[key] for key in columns))
        for row in data:
            print("  ".join(str(row.get(key, "")).ljust(widths[key]) for key in columns))
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


def watch(interval: float, iterations: int, json_output: bool, collector: Callable[[], list[InterfaceStats]] = interfaces) -> None:
    previous = {item.name: item for item in collector()}
    run = 0
    try:
        while iterations == 0 or run < iterations:
            time.sleep(interval)
            current = {item.name: item for item in collector()}
            rows = []
            for name, item in current.items():
                old = previous.get(name, item)
                rows.append({"interface": name, "state": item.state,
                             "rx_kib_s": round(max(0, item.rx_bytes - old.rx_bytes) / 1024 / interval, 2),
                             "tx_kib_s": round(max(0, item.tx_bytes - old.tx_bytes) / 1024 / interval, 2),
                             "errors": item.rx_errors + item.tx_errors})
            render(rows, json_output)
            previous, run = current, run + 1
    except KeyboardInterrupt:
        LOG.info("Monitoring beendet")


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="netcontrol", description="Sichere Netzwerkdiagnose und Echtzeitüberwachung")
    root.add_argument("--json", action="store_true", help="maschinenlesbare JSON-Ausgabe")
    root.add_argument("--config", metavar="DATEI", help="optionale TOML-Konfiguration")
    root.add_argument("--verbose", action="store_true", help="Debug-Protokollierung aktivieren")
    root.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    commands = root.add_subparsers(dest="command", required=True)
    commands.add_parser("status", help="kompletten Systemüberblick anzeigen")
    commands.add_parser("interfaces", help="Schnittstellen und Zähler anzeigen")
    commands.add_parser("routes", help="IPv4-Routingtabelle anzeigen")
    conn = commands.add_parser("connections", help="lokale TCP/UDP-Sockets anzeigen")
    conn.add_argument("--listening", action="store_true", help="nur lauschende TCP-Sockets")
    dns = commands.add_parser("dns", help="Hostnamen auflösen")
    dns.add_argument("host")
    check = commands.add_parser("check", help="gezielten TCP-Verbindungscheck ausführen")
    check.add_argument("host"); check.add_argument("port", type=int)
    check.add_argument("--timeout", type=float, default=None)
    probe = commands.add_parser("ping", help="Erreichbarkeit per System-Ping prüfen")
    probe.add_argument("host"); probe.add_argument("--count", type=int, default=None)
    probe.add_argument("--timeout", type=float, default=None)
    monitor = commands.add_parser("watch", help="Bandbreite fortlaufend beobachten")
    monitor.add_argument("--interval", type=float, default=None)
    monitor.add_argument("--iterations", type=int, default=0, help="0 bedeutet unbegrenzt")
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.WARNING,
                        format="%(levelname)s: %(message)s")
    try:
        config = load_config(args.config).get("netcontrol", {})
        timeout = args.timeout if hasattr(args, "timeout") and args.timeout is not None else float(config.get("timeout", 3.0))
        if args.command == "status": render(snapshot(), args.json)
        elif args.command == "interfaces": render([asdict(item) for item in interfaces()], args.json)
        elif args.command == "routes": render(routes(), args.json)
        elif args.command == "connections": render(connections(listening_only=args.listening), args.json)
        elif args.command == "dns": render(dns_lookup(args.host), args.json)
        elif args.command == "check":
            if not 1 <= args.port <= 65535: raise ValueError("Port muss zwischen 1 und 65535 liegen")
            result = tcp_check(args.host, args.port, timeout); render(result, args.json)
            return 0 if result["reachable"] else 2
        elif args.command == "ping":
            count = args.count if args.count is not None else int(config.get("ping_count", 3))
            if count < 1: raise ValueError("Count muss mindestens 1 sein")
            result = ping(args.host, count, timeout); render(result, args.json)
            return 0 if result["reachable"] else 2
        elif args.command == "watch":
            interval = args.interval if args.interval is not None else float(config.get("watch_interval", 2.0))
            if interval <= 0 or args.iterations < 0: raise ValueError("Intervall muss positiv und Iterationszahl nicht-negativ sein")
            watch(interval, args.iterations, args.json)
        return 0
    except (OSError, ValueError, RuntimeError, socket.gaierror) as exc:
        LOG.error("%s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())
