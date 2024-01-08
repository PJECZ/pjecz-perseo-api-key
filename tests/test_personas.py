"""
Unit tests for Personas
"""
import unittest

import requests

from tests.load_env import config


class TestPersonas(unittest.TestCase):
    """Tests for Personas"""

    def test_get_personas(self):
        """Test GET method for Personas"""
        response = requests.get(
            f"{config['api_base_url']}/personas",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)


if __name__ == "__main__":
    unittest.main()
