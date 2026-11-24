import json
import random
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)

QUOTES = json.loads((Path(__file__).parent / "quotes.json").read_text(encoding="utf-8"))


@app.get("/")
def index():
    return jsonify({
        "service": "Quotes API",
        "endpoints": [
            "/api/quotes",
            "/api/quotes/random",
            "/api/quotes/<int:id>",
        ],
    })


@app.get("/api/quotes")
def all_quotes():
    return jsonify(QUOTES)


@app.get("/api/quotes/random")
def random_quote():
    return jsonify(random.choice(QUOTES))


@app.get("/api/quotes/<int:quote_id>")
def get_quote(quote_id):
    for quote in QUOTES:
        if quote["id"] == quote_id:
            return jsonify(quote)
    return jsonify({"error": "Quote not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
