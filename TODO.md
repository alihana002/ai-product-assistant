# AI Product Assistant – TODO

## Ziel des Projekts

Eine moderne Python-Anwendung entwickeln, die zunächst Produkte verwaltet und später um LLM-Integration, Tool Calling, MCP, Agents und RAG erweitert wird.

Das Projekt dient gleichzeitig dazu, folgende Fähigkeiten praktisch zu lernen:

- Python sauber strukturieren
- Funktionen und Klassen sinnvoll designen
- Git im Projektalltag verwenden
- APIs und JSON verstehen
- LLMs aus Python ansprechen
- Structured Outputs verwenden
- Tool Calling implementieren
- MCP verstehen und einsetzen
- Agentische Workflows bauen
- RAG und Dokumentensuche integrieren
- Tests schreiben
- Docker-Grundlagen anwenden
- Ein vorzeigbares GitHub-Portfolio-Projekt erstellen

---

# Phase 0 – Projekt-Setup

## Git

- [x] Projektordner erstellen
- [x] Git-Repository initialisieren
- [x] `.gitignore` erstellen
- [x] Ersten Commit vorbereiten
- [x] Prüfen, ob `git status` sauber ist
- [ ] Initialen Commit abschließen: `Initial project setup`

## Python / uv

- [x] `uv` installieren
- [x] Projekt mit `uv init` initialisieren
- [x] `pyproject.toml` erzeugen
- [x] `.python-version` erzeugen
- [x] Package-Struktur unter `src/ai_product_assistant/` anlegen
- [x] Beschreibung in `pyproject.toml` anpassen
- [x] Mit `uv sync` Umgebung erzeugen
- [x] Prüfen, ob `.venv/` durch `.gitignore` ignoriert wird
- [x] Testweise Anwendung mit `uv run` starten

## Grundstruktur

Geplante Ausgangsstruktur:

```text
ai-product-assistant/
├── src/
│   └── ai_product_assistant/
│       ├── __init__.py
│       └── main.py
├── tests/
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

---

# Phase 1 – Produktverwaltung

## 1.1 Anforderungen definieren

- [ ] Festlegen, welche Informationen ein Produkt besitzt
- [ ] Mindestens folgende Felder verwenden:
  - [ ] `id`
  - [ ] `name`
  - [ ] `price`
  - [ ] `stock`
  - [ ] `category`
- [ ] Festlegen, wo die Produktdaten anfangs gespeichert werden
- [ ] Für Version 1 einfache Python-Liste mit Dictionaries verwenden

Beispielidee:

```python
products = [
    {
        "id": 1,
        "name": "Tisch",
        "price": 299.99,
        "stock": 8,
        "category": "Möbel",
    }
]
```

## 1.2 Produkt anhand einer ID finden

- [x] Funktion `get_product(product_id)` designen
- [x] Definieren, welchen Input die Funktion erwartet
- [x] Definieren, welchen Output die Funktion liefert
- [x] Produkte durchsuchen
- [x] Passendes Produkt zurückgeben
- [x] Verhalten definieren, wenn Produkt nicht existiert
- [x] Funktion manuell mit mehreren IDs testen

Fragen, die vor dem Coden beantwortet werden sollen:

- [x] Soll bei einer unbekannten ID `None` zurückgegeben werden?
- [x] Oder soll eine Exception ausgelöst werden?
- [x] Soll die Funktion direkt etwas ausgeben oder nur Daten zurückgeben?

Ziel: Die Funktion soll möglichst nur **eine Verantwortung** haben.

## 1.3 Benutzereingabe

- [x] Benutzer nach Produkt-ID fragen
- [x] Eingabe mit `input()` entgegennehmen
- [x] String in Integer umwandeln
- [x] Ungültige Eingaben behandeln
- [x] `get_product()` aufrufen
- [x] Ergebnis verständlich anzeigen

Zu lernende Themen:

- [x] `input()`
- [x] `int()`
- [x] `try / except`
- [x] Rückgabewerte von Funktionen

## 1.4 Weitere Produktfunktionen

Erst nach `get_product()` ergänzen:

- [x] `list_products()`
- [x] `search_product(name)`
- [x] `add_product(...)`
- [x] `update_stock(product_id, amount)`
- [x] `get_low_stock_products()`

Wichtig:

- [x] Nicht alle Funktionen gleichzeitig bauen
- [x] Nach jeder Funktion testen
- [x] Nach sinnvollen Schritten committen

Mögliche Commits:

```text
Add initial product data
Implement product lookup
Add product input validation
Add product search
Add stock management
```

---

# Phase 2 – Daten sauber speichern

## 2.1 JSON

- [ ] Produktdaten aus Python-Code herauslösen
- [ ] `products.json` anlegen
- [ ] JSON-Struktur verstehen
- [ ] Produkte aus JSON laden
- [ ] Änderungen zurück in JSON speichern

Zu lernende Themen:

- [x] `json.load()`
- [x] `json.dump()`
- [x] Datei öffnen mit `with open(...)`
- [x] Encoding
- [x] Dateipfade

## 2.2 Fehlerbehandlung

- [x] Fehlende Datei behandeln
- [x] Kaputte JSON-Datei behandeln
- [x] Ungültige Produktdaten erkennen
- [x]  Sinnvolle Fehlermeldungen erzeugen

---

# Phase 3 – Code strukturieren

Wenn `main.py` zu groß wird, aufteilen.

Mögliche spätere Struktur:

```text
src/
└── ai_product_assistant/
    ├── __init__.py
    ├── main.py
    ├── models.py
    ├── repository.py
    ├── services.py
    └── config.py
```

## 3.1 Verantwortlichkeiten verstehen

- [x] Erkennen, welche Funktionen zusammengehören

Funktionen die zsm gehören: Die json funktionen, dann die restlichen funktionen sind wahrscheinlich zsm 
- [x] Datenzugriff von Benutzeroberfläche trennen

- [x] Geschäftslogik von Ein-/Ausgabe trennen

wie recherchiert man dazu? 


- [x] Große Funktionen in kleinere Funktionen zerlegen
hab nicht so große funktionen dafür oder?

## 3.2 OOP erst bei echtem Bedarf

- [x] Prüfen, ob ein `Product`-Objekt sinnvoll ist
- [x] `Product` als Klasse oder Dataclass ausprobieren
- [x] Unterschied zwischen Dictionary und Objekt verstehen
- [x] Keine Klassen nur der Klassen wegen hinzufügen

### Aktueller Zwischenschritt: `Product` als Dataclass refactoren

- [x] `Product` als Dataclass definieren
- [x] Verstehen: JSON → Dictionary → `Product(**product_dict)` → Product-Objekt
- [x] JSON-Dictionaries beim Laden in `Product`-Objekte umwandeln
- [x] Services von `product["id"]` auf `product.id` umstellen
- [x] Tests auf Product-Objekte anpassen
- [x] Product-Objekte vor dem Speichern wieder in JSON-kompatible Dictionaries umwandeln

Zu lernende Themen:

- [x] Klassen
- [x] `__init__`
- [x] Methoden
- [x] `@dataclass`
- [x] Type Hints

---

# Phase 4 – Tests

## pytest einrichten

- [x] `pytest` als Development Dependency hinzufügen

```bash
uv add --dev pytest
```

- [x] Erste Testdatei erstellen
- [x] `get_product()` testen
- [x] Existierende ID testen
- [x] Nicht existierende ID testen
- [x] Ungültige Eingabe testen

Spätere Struktur:

```text
tests/
├── test_products.py
└── test_repository.py
```

- [x] Tests mit `uv run pytest` ausführen

---

# Phase 5 – APIs und HTTP

Bevor ein LLM eingebaut wird:

- [x] HTTP-Grundlagen verstehen
- [x] Request und Response verstehen
- [x] GET vs. POST verstehen
- [x] JSON über APIs senden und empfangen
- [x] Status Codes verstehen
- [x] API Keys verstehen
- [ ] Environment Variables verstehen

## Kleine Übung

- [x] Eine öffentliche Test-API aus Python aufrufen
- [x] Response prüfen
- [x] JSON auslesen
- [x] Fehlerfälle behandeln

### HTTP-Übungsfortschritt

- [x] Eine erfolgreiche `200`-Response untersuchen
- [x] Einen `404 Not Found`-Fall mit einer vollständigen API-URL auslösen
- [x] Fehlerdaten aus dem JSON-Body auslesen
- [x] `raise_for_status()` und `HTTPError` verstehen
- [x] Einen allgemeinen `RequestException`-Block ergänzen

## Nächstes Projektziel: externe Produkt-API lesen

Ziel: Produktdaten lesend von einer passenden öffentlichen API abrufen,
ohne die lokale JSON-Produktverwaltung zu ersetzen.

- [x] Öffentliche Produkt-API auswählen
- [x] Einen GET-Endpoint dokumentieren
- [x] Externe JSON-Daten untersuchen
- [x] Externe Felder mit `Product` vergleichen
- [x] Entscheiden, in welche Schicht der API-Zugriff gehört
- [x] HTTP- und Verbindungsfehler behandeln

### Umsetzung in kleinen Schritten

- [x] Ein API-Produkt-Dictionary im Notebook manuell in ein `Product`-Objekt umwandeln
- [x] Eine Notebook-Funktion mit `product_id: int` erstellen, die bei Erfolg ein `Product` zurückgibt
- [x] Bei `404 Not Found` gezielt `None` zurückgeben
- [x] Andere HTTP-Fehler von `404` unterscheiden
- [x] Einen simulierten `500 Server Error` testen und sicherstellen, dass er nicht als `None` behandelt wird
- [x] Verbindungsfehler verständlich behandeln, ohne sie als "Produkt nicht gefunden" auszugeben
- [x] Erfolgsfall mit einer vorhandenen API-ID testen
- [x] Nicht vorhandene API-ID testen und `None` prüfen
- [x] Erst danach die getestete Funktion nach `repository.py` übertragen
- [ ] Repository-Funktion anschließend separat mit pytest testen
- [ ] Erst nach dem Repository-Test entscheiden, ob ein CLI-Menüpunkt sinnvoll ist

---

# Phase 6 – LLM-Integration

## Vorbereitung

- [ ] Geeigneten LLM-Anbieter auswählen
- [ ] API-Key einrichten
- [ ] `.env` für Secrets verwenden
- [ ] Sicherstellen, dass `.env` nicht committed wird
- [ ] Kostenlimit beim Anbieter setzen

## Erste LLM-Anfrage

- [ ] SDK installieren
- [ ] Einfachen Prompt senden
- [ ] Antwort ausgeben
- [ ] Fehlerbehandlung ergänzen

Ziel:

```text
User
 ↓
Python
 ↓
LLM API
 ↓
Antwort
```

Zu lernende Begriffe:

- [ ] LLM
- [ ] Prompt
- [ ] System Prompt / Instructions
- [ ] Tokens
- [ ] Context Window
- [ ] Temperature
- [ ] Model
- [ ] Inference

---

# Phase 7 – Structured Outputs

Ziel: Das Modell soll keine beliebigen Texte liefern, sondern strukturierte Daten.

Beispiel:

```json
{
  "product_id": 3,
  "intent": "get_stock"
}
```

TODO:

- [ ] JSON-basierte Antworten verstehen
- [ ] Schema definieren
- [ ] Pydantic kennenlernen
- [ ] LLM-Ausgabe validieren
- [ ] Fehlerhafte Ausgaben behandeln

---

# Phase 8 – Tool Calling

Dies ist einer der wichtigsten Teile des Projekts.

## Erste Tools

Bestehende Python-Funktionen als Tools verwenden:

- [ ] `get_product`
- [ ] `search_product`
- [ ] `get_stock`

Zielablauf:

```text
User:
"Wie viel Bestand haben wir von Produkt 3?"

        ↓
       LLM
        ↓
erkennt passendes Tool
        ↓
get_stock(product_id=3)
        ↓
      Python
        ↓
    Ergebnis
        ↓
       LLM
        ↓
Antwort an Benutzer
```

TODO:

- [ ] Tool-Schema definieren
- [ ] Tool dem LLM bekannt machen
- [ ] Tool Call aus Modellantwort erkennen
- [ ] Python-Funktion anhand des Tool Calls aufrufen
- [ ] Ergebnis zurück ans Modell geben
- [ ] Endantwort erzeugen
- [ ] Falsche Tool-Argumente behandeln

---

# Phase 9 – Mehrere Tools und einfacher Agent

Tools erweitern:

- [ ] Produktinformationen
- [ ] Bestand
- [ ] Produktsuche
- [ ] Preis
- [ ] Statistiken

Agentischer Ablauf:

- [ ] Modell darf selbst das passende Tool auswählen
- [ ] Mehrere Tool Calls nacheinander ermöglichen
- [ ] Maximalzahl an Schritten festlegen
- [ ] Fehler und Endlosschleifen verhindern
- [ ] Tool-Ergebnisse protokollieren

Beispielaufgabe:

> Welches Produkt hat wenig Bestand und ist gleichzeitig besonders teuer?

Der Agent muss eventuell:

1. Produkte laden
2. Bestand prüfen
3. Preise vergleichen
4. Ergebnis zusammenfassen

---

# Phase 10 – SQL

Nach der JSON-Version:

- [ ] SQLite kennenlernen
- [ ] Produkttabelle anlegen
- [ ] Daten einfügen
- [ ] `SELECT` ausführen
- [ ] Repository auf SQL umstellen

Mögliche Tools:

- [ ] `get_product_from_db`
- [ ] `search_products`
- [ ] `get_low_stock_products`

Wichtig:

- [ ] Keine unkontrollierten LLM-generierten SQL-Statements direkt ausführen
- [ ] Parameterisierte Queries verwenden
- [ ] Schreibzugriffe begrenzen

---

# Phase 11 – MCP

Erst nach Tool Calling beginnen.

## Grundlagen

- [ ] Verstehen, welches Problem MCP löst
- [ ] MCP Host, Client und Server unterscheiden
- [ ] Tools vs. Resources verstehen
- [ ] MCP Python SDK installieren

## Eigener MCP Server

- [ ] Kleinen MCP Server erstellen
- [ ] `get_product` als MCP Tool anbieten
- [ ] `get_stock` als MCP Tool anbieten
- [ ] Server lokal starten
- [ ] MCP Client verbinden
- [ ] Tool Calls testen

Ziel:

```text
AI-Anwendung
     ↓
    MCP
     ↓
Product MCP Server
 ├── get_product
 ├── get_stock
 └── search_product
```

---

# Phase 12 – RAG

## Grundlagen

- [ ] Embeddings verstehen
- [ ] Semantic Search verstehen
- [ ] Chunking verstehen
- [ ] Retrieval verstehen
- [ ] Unterschied RAG vs. Training verstehen

## Umsetzung

- [ ] Beispiel-Produktdokumente hinzufügen
- [ ] Dokumente einlesen
- [ ] Texte in Chunks zerlegen
- [ ] Embeddings erzeugen
- [ ] Relevante Chunks finden
- [ ] Chunks an LLM weitergeben
- [ ] Quellen in Antworten angeben

Beispiel:

> Welche Garantiebedingungen gelten für Produkt 123?

---

# Phase 13 – Konfiguration und Sicherheit

- [ ] `.env` sauber einsetzen
- [ ] Keine API-Keys im Code
- [ ] Keine API-Keys auf GitHub
- [ ] Eingaben validieren
- [ ] Tool-Zugriffe begrenzen
- [ ] Schreibende Tools besonders absichern
- [ ] Logging ergänzen
- [ ] Fehler nicht mit sensiblen Daten ausgeben

---

# Phase 14 – Docker

- [ ] Docker-Grundlagen verstehen
- [ ] `Dockerfile` erstellen
- [ ] Anwendung containerisieren
- [ ] Container lokal starten
- [ ] Environment Variables übergeben
- [ ] `.dockerignore` erstellen

---

# Phase 15 – Qualität und Refactoring

- [ ] Doppelte Logik entfernen
- [ ] Funktionsnamen überprüfen
- [ ] Type Hints ergänzen
- [ ] Docstrings für wichtige Funktionen
- [ ] Fehlerbehandlung vereinheitlichen
- [ ] Logging statt unnötiger `print()`-Aufrufe verwenden
- [ ] Tests erweitern
- [ ] Projektstruktur überprüfen
- [ ] Abhängigkeiten aufräumen

---

# Phase 16 – README / Portfolio

README soll am Ende enthalten:

- [ ] Projektbeschreibung
- [ ] Motivation
- [ ] Features
- [ ] Architekturübersicht
- [ ] Technologien
- [ ] Installation mit `uv`
- [ ] Startanleitung
- [ ] Konfiguration / `.env.example`
- [ ] Beispielanfragen
- [ ] Tool-Calling-Erklärung
- [ ] MCP-Erklärung
- [ ] RAG-Erklärung
- [ ] Tests ausführen
- [ ] Screenshots oder Demo
- [ ] Bekannte Einschränkungen
- [ ] Mögliche Erweiterungen

---

# Phase 17 – Optional: UI

Erst wenn die Backend-Logik sauber funktioniert.

Optionen:

- [ ] einfache CLI behalten
- [ ] Streamlit testen
- [ ] FastAPI Backend bauen
- [ ] Web-Frontend anbinden

Nicht zu früh anfangen. Die AI-/Backend-Logik hat Vorrang.

---

# Empfohlene Reihenfolge

```text
1. Projekt-Setup
2. Product Manager
3. JSON
4. Struktur / OOP
5. Tests
6. APIs
7. LLM
8. Structured Outputs
9. Tool Calling
10. Agent
11. SQL
12. MCP
13. RAG
14. Sicherheit
15. Docker
16. Refactoring
17. README / Portfolio
18. Optional UI
```

---

# Lernregel für das Projekt

Bei jedem neuen Feature:

1. Problem in normaler Sprache beschreiben.
2. Input und Output definieren.
3. Aufgabe in kleine Teile zerlegen.
4. Erst dann Funktionen/Klassen überlegen.
5. Selbst ersten Lösungsversuch schreiben.
6. Testen.
7. Fehler verstehen.
8. Refactoren.
9. Commit erstellen.
10. Kurz dokumentieren, was gelernt wurde.

---

# Aktueller nächster Schritt

## `get_product(product_id)`

Noch nicht direkt die fertige Lösung übernehmen.

- [ ] Produktdaten definieren
- [ ] Überlegen, wie `get_product()` auf die Daten zugreift
- [ ] Input festlegen
- [ ] Output festlegen
- [ ] Verhalten bei unbekannter ID festlegen
- [ ] Eigene Implementierung versuchen
- [ ] Funktion testen
- [ ] Danach gemeinsam reviewen
- [ ] Commit erstellen
