from flask import Flask, jsonify
from flask_cors import CORS
from data import TREFWOORDEN

app = Flask(__name__)
CORS(app)

# Simuleer nieuwsartikelen
NIEUWSBRONNEN = [
    {"titel": "Maastricht breidt fietsenstallingen uit bij station", "bron": "AD", "datum": "2025-04-25"},
    {"titel": "Venlo verwelkomt 10.000 bezoekers op streekmarkt", "bron": "1Limburg", "datum": "2025-04-24"},
    {"titel": "Nieuwe wijk in Groningen gasloos opgeleverd", "bron": "NOS", "datum": "2025-04-23"},
    {"titel": "Limburger wint Europese wielermedaille", "bron": "De Limburger", "datum": "2025-04-22"},
    {"titel": "Gemeente Heerlen start jeugdcampagne", "bron": "NRC", "datum": "2025-04-21"},
]

@app.route('/')
def home():
    return "API werkt: Limburg Media Monitor"

@app.route('/search')
def search():
    resultaten = []
    for artikel in NIEUWSBRONNEN:
        titel_lower = artikel['titel'].lower()
        if any(trefwoord in titel_lower for trefwoord in TREFWOORDEN):
            resultaten.append(artikel)
    return jsonify(resultaten)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
