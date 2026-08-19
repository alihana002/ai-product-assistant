# AI Product Assistant -- Anwenderprozess

## Ziel

Dieses Dokument beschreibt den geplanten Ablauf des AI Product Assistant
**aus Sicht des Anwenders**.

# Version 1 -- Produktsuche über die Konsole

## Anwenderablauf

``` text
Programm starten
      ↓
Produkt-ID eingeben
      ↓
Eingabe prüfen
      ↓
Produkt suchen
      ↓
Produkt gefunden?
   ↙             ↘
 Ja              Nein
 ↓                ↓
Produktdaten    Fehlermeldung
anzeigen        anzeigen
```

### Beispiel: Produkt gefunden

``` text
AI Product Assistant

Bitte gib eine Produkt-ID ein: 2

Produkt gefunden:
ID: 2
Name: Stuhl
Preis: 99 €
```

### Beispiel: Produkt nicht gefunden

``` text
Bitte gib eine Produkt-ID ein: 99

Kein Produkt mit der ID 99 gefunden.
```

### Beispiel: Ungültige Eingabe

``` text
Bitte gib eine Produkt-ID ein: abc

Ungültige Eingabe. Bitte gib eine Zahl ein.
```

## Interner Ablauf

``` text
Benutzereingabe
      ↓
Eingabe validieren
      ↓
String → Integer
      ↓
get_product(product_id)
      ↓
Produkt oder None
      ↓
Ergebnis anzeigen
```

`get_product(product_id)` ist nur für die Suche zuständig. `main()`
steuert den Anwenderablauf, also Eingabe, Aufruf der Suche und Ausgabe.

# Aktuell nächster Entwicklungsschritt -- Benutzereingabe

Bisher wird eine ID beim Testen direkt im Code übergeben:

``` python
get_product(2)
```

Als Nächstes soll der Anwender sie selbst eingeben:

``` text
User gibt "2" ein
      ↓
Python erhält "2" als String
      ↓
Umwandlung in Integer
      ↓
get_product(2)
      ↓
Produkt oder None
      ↓
verständliche Ausgabe
```

## TODO

-   [x] Benutzer nach Produkt-ID fragen
-   [x] Eingabe mit `input()` entgegennehmen
-   [x] String in Integer umwandeln
-   [x] Ungültige Eingaben behandeln
-   [x] `get_product()` aufrufen
-   [x] Prüfen, ob ein Produkt gefunden wurde
-   [x] Produkt verständlich anzeigen
-   [] Bei unbekannter ID Fehlermeldung anzeigen

# Version 2 -- Produktmenü

Danach kann die Anwendung mehrere Aktionen anbieten:

``` text
AI Product Assistant

1 - Produkt über ID suchen
2 - Alle Produkte anzeigen
3 - Produkt über Namen suchen
4 - Programm beenden

Auswahl:
```

Geplante Zuordnung:

``` text
1 → get_product(product_id)
2 → list_products()
3 → search_product(name)
4 → Programm beenden
```

Später können `add_product`, `update_stock` und eine Suche nach
Produkten mit niedrigem Bestand hinzukommen.

# Version 3 -- Persistente Produktdaten

Die Bedienung bleibt ähnlich, aber die Produktdaten werden aus einer
Datei statt direkt aus dem Python-Code geladen:

``` text
Anwender
   ↓
Programm
   ↓
products.json
```

# Version 4 -- AI Product Assistant

Später soll der Anwender natürliche Sprache verwenden können:

``` text
"Wie teuer ist der Stuhl?"
"Zeig mir Produkt 3."
"Welche Produkte haben wenig Bestand?"
```

Ablauf:

``` text
Benutzerfrage
     ↓
    LLM
     ↓
Absicht erkennen
     ↓
passende Funktion auswählen
     ↓
Python-Funktion ausführen
     ↓
Ergebnis
     ↓
LLM formuliert Antwort
     ↓
Benutzer
```

# Version 5 -- Tool Calling

Die Python-Funktionen werden als Tools verfügbar gemacht.

``` text
User: "Wie viel kostet Produkt 2?"
        ↓
LLM wählt get_product
        ↓
get_product(product_id=2)
        ↓
{"id": 2, "name": "Stuhl", "price": 99}
        ↓
LLM
        ↓
"Der Stuhl kostet 99 €."
```

Die KI soll die Produktdaten also nicht erfinden, sondern die dafür
vorgesehene Funktion aufrufen.

# Version 6 -- MCP

Später werden die Produktfunktionen über einen MCP Server angeboten:

``` text
Benutzer
   ↓
AI-Anwendung
   ↓
LLM
   ↓
MCP Client
   ↓
MCP Server
   ↓
get_product / get_stock / search_product
   ↓
Produktdaten
```

# Langfristiger Anwenderprozess

``` text
User:
"Welche Möbel haben weniger als 5 Stück auf Lager?"

        ↓

Assistant:
"Zwei Produkte haben einen niedrigen Bestand:
- Schrank – 3 Stück
- Tisch – 2 Stück"
```

Intern:

``` text
Natürliche Sprache
       ↓
      LLM
       ↓
Tool Calling / MCP
       ↓
Produktlogik
       ↓
JSON / Datenbank
       ↓
Ergebnis
       ↓
      LLM
       ↓
verständliche Antwort
```

# Entwicklungsstand

``` text
[✓] Produktdaten als Liste von Dictionaries
[✓] get_product(product_id)
[✓] Produkt über ID suchen
[✓] Produkt oder None zurückgeben

        ↓ JETZT

[ ] Benutzereingabe
[ ] Eingabevalidierung
[ ] Ergebnisanzeige

        ↓ DANACH

[ ] Weitere Produktfunktionen
[ ] JSON-Speicherung
[ ] Tests
[ ] LLM-Integration
[ ] Tool Calling
[ ] MCP
[ ] RAG
```

## Nächstes konkretes Ziel

**Programm starten → Produkt-ID eingeben → Eingabe prüfen → Produkt
suchen → Ergebnis anzeigen.**

Erst danach erweitern wir die Produktverwaltung um weitere Funktionen.
