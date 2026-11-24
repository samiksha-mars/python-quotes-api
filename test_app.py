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


if __name__ == "__main__":
    unittest.main()
