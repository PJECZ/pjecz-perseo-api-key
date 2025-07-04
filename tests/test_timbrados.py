"""
Unit tests for timbrados
"""

import unittest

import requests

from tests import config


class TestTimbrados(unittest.TestCase):
    """Tests for Timbrados"""

    def test_get_timbrado_by_curp(self):
        # Consultar
        try:
            response = requests.get(
                f"{config['api_base_url']}/api/v5/timbrados?curp={config['curp']}",
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

    def test_get_timbrados(self):
        # Consultar
        try:
            response = requests.get(
                f"{config['api_base_url']}/api/v5/timbrados",
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
