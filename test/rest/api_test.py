import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add(self):
        response = self.app.get('/calc/add/1/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 3)
    
    def test_add_invalid(self):
        response = self.app.get('/calc/add/1/a')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)
    
    # Similar tests for other operations...

if __name__ == '__main__':
    unittest.main()
