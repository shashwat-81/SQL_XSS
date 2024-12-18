import unittest
from middleware.scraper import scrape_input_fields

class TestScraper(unittest.TestCase):
    def test_valid_url(self):
        url = "http://127.0.0.1:8080/WebGoat"  # Use a known test URL
        fields = scrape_input_fields(url)
        self.assertIsInstance(fields, list)
        for field in fields:
            self.assertIn('name', field)
            self.assertIn('type', field)

    def test_invalid_url(self):
        url = "https://invalid-url.com"
        fields = scrape_input_fields(url)
        self.assertEqual(fields, [])

if __name__ == "__main__":
    unittest.main()
