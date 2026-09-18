# AI Product Assistant – JSON Phase TODO

## Ziel dieser Zwischenphase

Die Produktdaten sollen nicht mehr fest im Python-Code stehen, sondern aus einer `products.json` geladen und nach Änderungen dauerhaft gespeichert werden.

Der zentrale Datenfluss:

```text
Programm startet
    ↓
products.json laden
    ↓
Python-Liste `products`
    ↓
Funktionen arbeiten mit der Liste
    ↓
Änderung erfolgreich?
    ↓
products.json speichern
```

# 1. JSON-Datei vorbereiten

- [x] Ordner `data/` erstellen
- [x] Datei `data/products.json` erstellen
- [x] aktuelle Produktdaten aus Python in JSON übertragen
- [x] prüfen, ob jedes Produkt dieselben Felder besitzt:
  - [x] `id`
  - [x] `name`
  - [x] `price`
  - [x] `stock`
- [x] JSON-Datei einmal manuell öffnen und Struktur prüfen

Beispiel:

```json
[
  {
    "id": 1,
    "name": "Tisch",
    "price": 299,
    "stock": 5
  },
  {
    "id": 2,
    "name": "Stuhl",
    "price": 99,
    "stock": 10
  }
]
```

# 2. `load_products()` bauen

Ziel:

```text
products.json
    ↓
json.load()
    ↓
Python-Liste
```

TODO:

- [x] `import json`
- [x] Pfad zur JSON-Datei festlegen
- [x] Datei mit `with open(..., "r", encoding="utf-8")` öffnen
- [x] Daten mit `json.load()` lesen
- [x] geladene Liste zurückgeben
- [x] Funktion separat testen

Erwartetes Verhalten:

```python
products = load_products()
```

# 3. `save_products(products)` bauen

Ziel:

```text
Python-Liste
    ↓
json.dump()
    ↓
products.json
```

TODO:

- [x] Datei im Schreibmodus `"w"` öffnen
- [x] `encoding="utf-8"` verwenden
- [x] `json.dump()` verwenden
- [x] `indent=2` oder `indent=4` für lesbares JSON verwenden
- [x] Funktion separat testen
- [x] prüfen, ob Umlaute korrekt gespeichert werden

# 4. Bestehende Funktionen mit geladenen Daten testen

Diese Funktionen ändern keine Daten und müssen deshalb nicht speichern:

- [x] `get_product()` mit geladenen JSON-Daten testen
- [x] `list_products()` mit geladenen JSON-Daten testen
- [x] `search_product()` mit geladenen JSON-Daten testen
- [x] `get_low_stock_products()` mit geladenen JSON-Daten testen

# 5. `add_product()` persistent machen

Ziel:

```text
add_product()
→ Produkt zur Liste hinzufügen
→ aktualisierte Liste speichern
```

TODO:

- [x] Produkt wie bisher als Dictionary erstellen
- [x] mit `append()` zur Liste hinzufügen
- [x] nach erfolgreichem Hinzufügen `save_products(products)` ausführen
- [x] Programm beenden
- [x] Programm neu starten
- [x] prüfen, ob das neue Produkt noch vorhanden ist

# 6. `update_stock()` persistent machen

Ziel:

```text
update_stock()
→ Bestand ändern
→ aktualisierte Produktliste speichern
```

TODO:

- [x] Produkt anhand der ID finden
- [x] neuen Bestand setzen
- [x] geändertes Produkt zurückgeben
- [x] nach erfolgreicher Änderung `save_products(products)` aufrufen
- [x] Programm neu starten
- [x] prüfen, ob der neue Bestand erhalten bleibt

# 7. Wo soll `save_products()` aufgerufen werden?

Für die erste Version:

```text
main()
  ↓
add_product()
  ↓
wenn erfolgreich
  ↓
save_products(products)
```

und:

```text
main()
  ↓
update_stock()
  ↓
wenn erfolgreich
  ↓
save_products(products)
```

Damit bleiben die Verantwortlichkeiten verständlich:

```text
get_product() / search_product()
→ suchen

add_product() / update_stock()
→ Daten im Speicher verändern

load_products()
→ Datei lesen

save_products()
→ Datei schreiben

main()
→ Ablauf steuern
```

Später kann man das in `repository.py` oder `services.py` trennen.

# 8. Fehlerbehandlung erst danach

Erst wenn Lesen und Schreiben grundsätzlich funktionieren:

- [x] `FileNotFoundError` bei fehlender JSON-Datei behandeln
- [x] `json.JSONDecodeError` bei kaputter JSON-Datei behandeln
- [x] sinnvolle Fehlermeldungen ausgeben
- [x] entscheiden, ob bei fehlender Datei eine leere Liste verwendet werden soll
- [x]
- verhindern, dass kaputte Daten versehentlich überschrieben werden

# 9. Manuelle Tests

## Test A – Laden
- [x] Programm starten
- [x] Produktliste wird aus JSON geladen
- [x] `get_product()` funktioniert

## Test B – Produkt hinzufügen
- [x] neues Produkt hinzufügen
- [x] Programm beenden
- [x] erneut starten
- [x] Produkt ist weiterhin vorhanden

## Test C – Bestand ändern
- [x] Stock eines Produkts ändern
- [x] Programm beenden
- [x] erneut starten
- [x] neuer Stock ist weiterhin vorhanden

## Test D – Low Stock
- [x] Bestände aus JSON laden
- [x] `get_low_stock_products()` ausführen
- [x] richtige Produkte werden zurückgegeben

# 10. Danach

```text
JSON-Persistenz ✅
    ↓
Code strukturieren
    ↓
Tests mit pytest
    ↓
APIs
    ↓
LLM
```

# Aktuell nächster Schritt

- [x] `data/products.json` anlegen
- [x] bestehende Produktliste dorthin übertragen
- [x] `load_products()` selbst implementieren
- [x] `load_products()` testen

Noch nicht gleichzeitig `save_products()`, Fehlerbehandlung und Refactoring bauen.
