"""
Unit tests for Puestos
"""
import unittest

import requests

from tests.load_env import config


class TestPuestos(unittest.TestCase):
    """Tests for Puestos"""

    def test_get_puestos(self):
        """Test GET method for Puestos"""
        response = requests.get(
            f"{config['api_base_url']}/puestos",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)


if __name__ == "__main__":
    unittest.main()
