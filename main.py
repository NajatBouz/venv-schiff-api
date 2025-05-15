
from flask import Flask, jsonify, request

app = Flask(__name__)

# Beispiel-Daten
schiffe = [
    {"name": "Titanic", "typ": "Passagierschiff", "baujahr": 1912},
    {"name": "Bismarck", "typ": "Schlachtschiff", "baujahr": 1939},
    {"name": "Queen Mary 2", "typ": "Kreuzfahrtschiff", "baujahr": 2003}
    {"name": "Babuschka 8", "typ": "Kreuzfahrtschiff", "baujahr": 2011}
]

@app.route('/')
def schiff():
    return 'Hallo, das ist eine Schiff-Api'

## GET-Route implementieren, d.h. Daten abrufen bzw. alle schiffe anzeigen
@app.route("/api/schiffe", methods=['GET'])
def show_schiff():
    return jsonify(), 200
## POST-Route implementieren, d.h. neues schiff hinzufügen
@app.route("/api/schiffe", methods=['POST'])
def add_schiffe():
    ## Funktion um die Daten im JSON-Format aus dem Request-Objekt zu bekommen
    new_schiff = request.get_json() # Hole dir aus dem Request-Objekt die Daten im JSON-Format
    # { "id": 3, "name": .., "age": ..., "type": ...}
    schiffe.append(new_schiff) # hänge das Objekt im JSON-Format hinten dran
    return f"{new_schiff} wurde erfolgreich hinzugefügt", 201
## DELETE-Route, um ein schiff aus der Liste zu löschen
@app.route("/api/schiffe/<name>", methods=['DELETE'])
def delete_schiff(name):
    for schiff in schiffe:
        if schiffe["name"] == name:
            schiffe.remove(schiff)
            return f"{name} wurde gelöscht", 200
    return f"{name} wurde nicht gefunden", 404
## Baue eine Funktion, zum Updaten
## PUT-Route -> Ersetze alle Eigenschaften eines schiffes (Eigenschaften im Body als JSON)
@app.route("/api/schiffe/<name>", methods=['PUT'])
def put_schiff(name):
    data = request.get_json()
    for schiff in schiffe:
        if schiff["name"] == name:
            schiff.clear() # Lösche alle Werte des gefundenen schiffes
            schiff.update(data) # Werte, die im JSON-Format in der Variablen data gespeichert sind
            return f"{name} wurde geupdated", 200
    return f"{name} wurde nicht gefunden", 404
## PATCH-Route -> Ersetze spezifisch einzelne Eigenschaften, d.h. hier schicken wir nur die zu ändernden Eigenschaften im Body als JSON mit
@app.route("/api/schiffe/<name>", methods=["PATCH"])
def patch_schiff(name):
    data = request.get_json()
    for schiff in schiffe:
        if schiff["name"] == name:
            schiff.update(data)
            return f"{name} wurde geupdatet", 200
    return f"{name} wurde nicht gefunden", 404

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5050, debug=True)
