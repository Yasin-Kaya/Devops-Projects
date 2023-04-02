import unittest
from app import app, convert

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_convert(self):
        self.assertEqual(convert(1), 'I')
        self.assertEqual(convert(9), 'IX')
        self.assertEqual(convert(49), 'XLIX')
        self.assertEqual(convert(99), 'XCIX')
        self.assertEqual(convert(999), 'CMXCIX')
        self.assertEqual(convert(3999), 'MMMCMXCIX')

    def test_valid_input(self):
        response = self.app.post('/', data=dict(number='5000'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Not Valid! Please enter a number between 1 and 3999, inclusively.', response.data)

    def test_invalid_input(self):
        response = self.app.post('/', data=dict(number='abc'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Not Valid! Please enter a number between 1 and 3999, inclusively.', response.data)

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please enter a number:', response.data)

    def test_result_page(self):
        response = self.app.post('/', data=dict(number='2022'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'2022', response.data)
        self.assertIn(b'MMXXII', response.data)

if __name__ == '__main__':
    unittest.main()
