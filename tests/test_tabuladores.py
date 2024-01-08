"""
Unit tests for Tabuladores
"""
import unittest

import requests

from tests.load_env import config


class TestTabuladores(unittest.TestCase):
    """Tests for Tabuladores"""

    def test_get_tabuladores(self):
        """Test GET method for Tabuladores"""
        response = requests.get(
            f"{config['api_base_url']}/tabuladores",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)

    def test_get_tabulador_by_id(self):
        """Test GET method for Tabuladores by id"""
        response = requests.get(
            f"{config['api_base_url']}/tabuladores/1",
            headers={"X-Api-Key": config["api_key"]},
            timeout=config["timeout"],
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["success"], True)
        self.assertEqual(data["id"], 1)


if __name__ == "__main__":
    unittest.main()
