import os
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from backend.main import app


class TestGenerateEndpoint(unittest.TestCase):
    @patch.dict(os.environ, {"GEMINI_API_KEY": ""}, clear=False)
    def test_generate_without_api_key_returns_clear_error(self):
        client = TestClient(app)
        response = client.post(
            "/generate",
            json={
                "document_type": "Rental Agreement",
                "user_details": "Landlord: Ravi Kumar. Tenant: Arun Kumar. Property: Chennai.",
            },
        )

        self.assertEqual(response.status_code, 503)
        self.assertIn("GEMINI_API_KEY", response.json()["detail"])


if __name__ == "__main__":
    unittest.main()
