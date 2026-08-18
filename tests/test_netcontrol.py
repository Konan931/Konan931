import socket
import tempfile
import threading
import unittest
from pathlib import Path

import netcontrol


class NetControlTests(unittest.TestCase):
    def test_interfaces_parses_proc_counters(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            proc = root / "dev"
            proc.write_text("Inter-| Receive | Transmit\n face |bytes packets errs drop fifo frame compressed multicast|bytes packets errs drop fifo colls carrier compressed\n  eth0: 100 2 3 0 0 0 0 0 400 5 6 0 0 0 0 0\n")
            sys = root / "sys" / "eth0"
            sys.mkdir(parents=True)
            (sys / "operstate").write_text("up\n")
            (sys / "mtu").write_text("1500\n")
            (sys / "address").write_text("aa:bb:cc:dd:ee:ff\n")
            item = netcontrol.interfaces(proc, root / "sys")[0]
            self.assertEqual((item.name, item.rx_bytes, item.tx_errors), ("eth0", 100, 6))

    def test_routes_decodes_linux_route(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "route"
            path.write_text("Iface Destination Gateway Flags RefCnt Use Metric Mask MTU Window IRTT\neth0 00000000 0102A8C0 0003 0 0 100 00000000 0 0 0\n")
            self.assertEqual(netcontrol.routes(path)[0]["gateway"], "192.168.2.1")

    def test_tcp_check_reaches_local_listener(self):
        server = socket.socket()
        server.bind(("127.0.0.1", 0)); server.listen(1)
        port = server.getsockname()[1]
        worker = threading.Thread(target=lambda: server.accept()[0].close())
        worker.start()
        result = netcontrol.tcp_check("127.0.0.1", port, 1)
        worker.join(); server.close()
        self.assertTrue(result["reachable"])

    def test_connection_summary(self):
        items = [{"protocol": "tcp", "state": "LISTEN"}, {"protocol": "tcp", "state": "LISTEN"}]
        self.assertEqual(netcontrol._connection_summary(items), {"tcp:LISTEN": 2})

    def test_invalid_port_is_rejected(self):
        self.assertEqual(netcontrol.main(["check", "localhost", "0"]), 1)


if __name__ == "__main__":
    unittest.main()
