from flask import Flask
from flask_cors import CORS  # <-- Dit toevoegen!

app = Flask(__name__)
CORS(app)  # <-- Dit toevoegen!

@app.route('/')
def home():
    return "API werkt: Limburg Media Monitor"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
