"""
Unit tests for personas
"""

import unittest

import requests

from tests import config


class TestPersonas(unittest.TestCase):
    """Tests for Personas"""

    def test_get_personas(self):
        """Test GET method for personas"""

        # Consultar
        try:
            response = requests.get(
                f"{config['api_base_url']}/api/v5/personas",
                headers={"X-Api-Key": config["api_key"]},
                timeout=config["timeout"],
            )
        except requests.exceptions.RequestException as error:
            self.fail(error)
        self.assertEqual(response.status_code, 200)

        # Validar el contenido de la respuesta
        contenido = response.json()
        self.assertEqual("success" in contenido, True)
        self.assertEqual("message" in contenido, True)
        self.assertEqual("data" in contenido, True)

        # Validar que se haya tenido éxito
        self.assertEqual(contenido["success"], True)

        # Validar los datos
        self.assertEqual(type(contenido["data"]), list)


if __name__ == "__main__":
    unittest.main()
