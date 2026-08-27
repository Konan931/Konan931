# NetControl

Ein kompaktes, sicheres Network-Control-Tool für Linux: Systemüberblick,
Schnittstellenstatistiken, Routing, lokale Verbindungen, DNS, Ping,
gezielte TCP-Checks und Live-Bandbreitenmonitoring – ohne externe
Python-Abhängigkeiten.

## Schnellstart

```bash
python3 tools/netcontrol/netcontrol.py status
python3 tools/netcontrol/netcontrol.py interfaces
python3 tools/netcontrol/netcontrol.py routes
python3 tools/netcontrol/netcontrol.py connections --listening
python3 tools/netcontrol/netcontrol.py dns example.org
python3 tools/netcontrol/netcontrol.py check example.org 443 --timeout 2
python3 tools/netcontrol/netcontrol.py ping 1.1.1.1 --count 3
python3 tools/netcontrol/netcontrol.py watch --interval 1
```

`--json` gehört vor den Unterbefehl und liefert stabile, maschinenlesbare
Ausgaben, etwa `python3 tools/netcontrol/netcontrol.py --json status`.
`--verbose` aktiviert Diagnoselogs. Exitcode `0` steht für Erfolg, `2` für
einen nicht erreichbaren Ping/TCP-Endpunkt und `1` für Eingabe- oder
Laufzeitfehler.

## Konfiguration

Die optionale TOML-Datei setzt Standardwerte:

```bash
cp tools/netcontrol/netcontrol.toml.example tools/netcontrol/netcontrol.toml
python3 tools/netcontrol/netcontrol.py \
  --config tools/netcontrol/netcontrol.toml status
```

CLI-Optionen überschreiben die Konfiguration. Python 3.11 oder neuer wird
empfohlen. Die Systeminformationen stammen aus `/proc` und `/sys`; auf anderen
Betriebssystemen bleiben DNS und TCP-Checks nutzbar, während Linux-spezifische
Tabellen leer sein können. Der Ping-Befehl benötigt das lokale `ping`-Programm.

## Sicherheit

NetControl verändert weder Firewall, Routen noch Schnittstellen. Der TCP-Check
prüft genau den angegebenen Host und Port; es gibt bewusst keinen Portscanner.
Für die normalen Funktionen sind keine Root-Rechte erforderlich. Teile
prozessfremder Socket-Informationen können abhängig von den Systemrechten fehlen.

## Entwicklung

```bash
python3 -m unittest discover -s tools/netcontrol/tests -v
python3 -m py_compile tools/netcontrol/netcontrol.py
```
