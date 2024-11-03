import unittest
from flask import Flask
from io import BytesIO
from app import app  # Import your Flask app


class TestChatApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the Flask test client
        cls.client = app.test_client()

    def test_upload_pdf(self):
        """Test PDF upload endpoint with a sample PDF file."""
        data = {
            'file': (BytesIO(b'%PDF-1.4 sample PDF content'), 'pytorch.pdf')
        }
        response = self.client.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.get_json())  # Check if 'success' key is in response

    def test_query_pdf_content(self):
        """Test querying the PDF content with a sample question."""
        question_data = {
            "question": "what is deep Learning "
        }
        response = self.client.post('/query', json=question_data)
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()

        # Check that response contains expected keys
        self.assertIn('response', response_data)
        self.assertIsInstance(response_data['response'], str)

    def test_empty_question(self):
        """Test querying with an empty question."""
        question_data = {
            "question": ""
        }
        response = self.client.post('/query', json=question_data)
        self.assertEqual(response.status_code, 400)  # Expecting a 400 error for empty question
        response_data = response.get_json()

        # Check for error message
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], "Question cannot be empty")

    def test_invalid_file_upload(self):
        """Test PDF upload with a non-PDF file."""
        data = {
            'file': (BytesIO(b'Not a PDF content'), 'sample.txt')
        }
        response = self.client.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 400)  # Expecting a 400 error for invalid file
        response_data = response.get_json()

        # Check for error message
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], "Only PDF files are allowed")


if __name__ == '__main__':
    unittest.main()
