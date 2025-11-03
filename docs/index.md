# Nummernsender im Internet - Seminar Dokumentation

Willkommen zur Dokumentation des Seminarprojekts "Nummernsender im Internet"!

## Überblick

Dieses Projekt kombiniert Webentwicklung, API-Design und IoT-Programmierung, um ein vollständiges System für die Übertragung von Zahlen über das Internet zu erstellen.

### Was ist ein Nummernsender?

Ein Nummernsender ist ein System, das automatisch Zahlen in einer festgelegten Sequenz überträgt. In diesem Projekt implementieren wir:

- **Web-Anwendung**: Interaktive Webseite zur Anzeige der Zahlen
- **API**: Maschinenlesbare Schnittstelle für den Zugriff auf die Zahlen
- **IoT-Integration**: Raspberry Pi Pico W Programme zum Empfangen und Anzeigen der Zahlen

## Projektziele

1. ✅ **Webentwicklung**: Moderne Flask-Anwendung mit responsive Design
2. ✅ **API-Design**: RESTful API mit JSON-Responses
3. ✅ **IoT-Programmierung**: MicroPython auf Raspberry Pi Pico W
4. ✅ **WiFi-Integration**: Drahtlose Kommunikation und Datenübertragung
5. ✅ **Dokumentation**: Vollständige Anleitungen und Troubleshooting

## Hauptkomponenten

### 1. Nummernsender Web-Anwendung

Eine interaktive Webseite, die Zahlen von 1-9 anzeigt und automatisch jede Sekunde wechselt.

**Features:**
- Responsive Design (funktioniert auf allen Geräten)
- Start/Stop/Reset-Steuerung
- Visuelle Anzeige der aktuellen Zahl
- Zykluszähler

**Technologien:**
- Python Flask
- HTML5 / CSS3
- JavaScript (Vanilla)

[→ Zur Web-App Dokumentation](web-app/web-app.md)

### 2. Nummernsender API

Eine RESTful API für maschinellen Zugriff auf die Zahlenübertragung.

**Endpoints:**
- `GET /api/number` - Aktuelle Zahl abrufen
- `GET /api/sequence` - Sequenz-Informationen
- `GET /api/status` - API-Status und Uptime

**Technologien:**
- Python Flask
- Flask-CORS für Cross-Origin Requests
- JSON Responses

[→ Zur API Dokumentation](web-app/api.md)

### 3. Raspberry Pi Pico Beispiele

Sechs vollständige MicroPython-Programme für verschiedene Anwendungsfälle:

| Programm | Beschreibung |
|----------|--------------|
| `01_blink.py` | Grundlegendes LED-Blinken |
| `02_wifi_connect.py` | WiFi-Verbindung herstellen und Status anzeigen |
| `03_wifi_signal_monitor.py` | Signalstärke messen und auf Console ausgeben |
| `04_wifi_signal_to_blink.py` | Signalstärke in Blinkfrequenz umwandeln |
| `05_api_consumer.py` | API abfragen und Ergebnis anzeigen |
| `06_access_point_web.py` | Als Access Point mit Web-Interface |

[→ Zu den Pico Beispielen](pico/introduction.md)

## Schnellstart

### Voraussetzungen

- Python 3.12+ installiert
- Raspberry Pi Pico W (für IoT-Beispiele)
- Thonny IDE (für Pico-Programmierung)
- Moderne Webbrowser

### Installation in 5 Schritten

1. **Repository klonen**
   ```bash
   git clone <repository-url>
   cd ws_internet_calling
   ```

2. **Virtuelle Umgebung erstellen**
   ```bash
   uv venv --seed
   source .venv/bin/activate  # macOS/Linux
   # oder
   .venv\Scripts\activate     # Windows
   ```

3. **Abhängigkeiten installieren**
   ```bash
   uv add flask flask-cors requests mkdocs mkdocs-material
   ```

4. **Web-Anwendung starten**
   ```bash
   python src/web_app/app.py
   # Öffne http://localhost:5000
   ```

5. **API starten** (in neuem Terminal)
   ```bash
   python src/api/app.py
   # API läuft auf http://localhost:5001
   ```

[→ Ausführlicher Schnellstart](getting-started/quickstart.md)

## Lernziele

Nach Abschluss dieses Projekts können Sie:

- ✅ Flask-Webanwendungen entwickeln
- ✅ RESTful APIs entwerfen und implementieren
- ✅ Raspberry Pi Pico W programmieren
- ✅ WiFi-Verbindungen in MicroPython herstellen
- ✅ API-Daten konsumieren und verarbeiten
- ✅ Access Points erstellen und Web-Interfaces bereitstellen
- ✅ Umfassende Dokumentationen schreiben

## Dokumentationsstruktur

### 📚 Getting Started
Erste Schritte, Übersicht und Schnellstart-Anleitung

### 🔧 Installation Guides
Detaillierte Installationsanleitungen für Thonny und Pico-Flashing

### 🌐 Web Applications
Dokumentation der Web-App und API

### 🤖 Raspberry Pi Pico
Alle Pico-Programme mit ausführlichen Erklärungen

### 🔍 Troubleshooting
Lösungen für häufige Probleme und FAQ

### 📖 Reference
API-Referenz, Code-Beispiele und zusätzliche Ressourcen

## Projektstruktur

```
ws_internet_calling/
├── src/
│   ├── web_app/           # Flask Web-Anwendung
│   │   ├── app.py
│   │   ├── templates/
│   │   └── static/
│   ├── api/               # Flask API
│   │   └── app.py
│   └── pico_scripts/      # Raspberry Pi Pico Programme
│       ├── 01_blink.py
│       ├── 02_wifi_connect.py
│       ├── 03_wifi_signal_monitor.py
│       ├── 04_wifi_signal_to_blink.py
│       ├── 05_api_consumer.py
│       └── 06_access_point_web.py
├── docs/                  # Dokumentation
│   ├── guides/
│   ├── troubleshooting/
│   └── reference/
├── examples/              # Beispiel-Code
│   └── api_client.py
├── mkdocs.yml            # MkDocs Konfiguration
├── pyproject.toml        # Python Projekt-Konfiguration
└── README.md             # Projekt-Readme
```

## Hilfe & Support

### Dokumentation durchsuchen
Nutzen Sie die Suchfunktion oben rechts, um schnell Informationen zu finden.

### Häufige Probleme
Schauen Sie in den [Troubleshooting Guide](troubleshooting/common_issues.md) für Lösungen.

### Community Ressourcen
- [Raspberry Pi Forums](https://forums.raspberrypi.com/)
- [MicroPython Forum](https://forum.micropython.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## Lizenz und Credits

Dieses Projekt wurde im Rahmen des Seminars "Nummernsender im Internet" entwickelt.

**Verwendete Technologien:**
- Python 3.12
- Flask & Flask-CORS
- MicroPython
- MkDocs & Material Theme
- Raspberry Pi Pico W

## Nächste Schritte

Bereit loszulegen? Hier sind einige Vorschläge:

1. [📋 Prerequisites überprüfen](getting-started/prerequisites.md)
2. [🚀 Schnellstart durchführen](getting-started/quickstart.md)
3. [💻 Thonny installieren](guides/thonny_installation.md)
4. [🔌 Pico flashen](guides/pico_flashing.md)
5. [🎯 Erstes Beispiel ausprobieren](pico/examples/blink.md)

---

**Viel Erfolg mit dem Projekt!** 🎉
