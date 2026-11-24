# Python Quotes API

A tiny REST API that serves programming and motivational quotes, built with Flask.
Quotes are loaded from a local `quotes.json` file.

## Endpoints

| Method | Path                 | Description                       |
|--------|----------------------|-----------------------------------|
| GET    | `/`                  | Service info and endpoint list    |
| GET    | `/api/quotes`        | All quotes                        |
| GET    | `/api/quotes/random` | A single random quote             |
| GET    | `/api/quotes/<id>`   | A specific quote by id (404 if missing) |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
python3 app.py
# or
flask --app app run
```

The API is available at http://localhost:5000.

### Example

```bash
curl http://localhost:5000/api/quotes/random
```

```json
{"id": 3, "text": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"}
```

## Tests

```bash
python3 -m unittest test_app.py
```
