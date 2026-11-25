import unittest

from app import app


class QuotesApiTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["service"], "Quotes API")

    def test_all_quotes(self):
        response = self.client.get("/api/quotes")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)
        self.assertGreater(len(response.get_json()), 0)

    def test_random_quote(self):
        response = self.client.get("/api/quotes/random")
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertIn("text", body)
        self.assertIn("author", body)

    def test_get_quote_by_id(self):
        response = self.client.get("/api/quotes/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], 1)

    def test_quote_not_found(self):
        response = self.client.get("/api/quotes/99999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json(), {"error": "Quote not found"})

    def test_unknown_route_returns_json(self):
        for path in ("/api/quotes/abc", "/api/nope"):
            response = self.client.get(path)
            self.assertEqual(response.status_code, 404)
            self.assertIn("error", response.get_json())

    def test_wrong_method_returns_json(self):
        response = self.client.post("/api/quotes")
        self.assertEqual(response.status_code, 405)
        self.assertIn("error", response.get_json())
        self.assertIn("GET", response.headers["Allow"])


if __name__ == "__main__":
    unittest.main()
