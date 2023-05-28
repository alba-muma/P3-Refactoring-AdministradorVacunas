"""Clase para la validacion de las keys de un json"""

import json
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException


class JsonParser:
    """Clase para la validacion de las keys de un json"""
    _key_list = []
    _key_error_message = []
    _error_message_json_not_found = "File is not found"
    _error_message_json_decode = "JSON Decode Error - Wrong JSON Format"
    def __init__(self, input_file):
        self._json_content = self._read_json_file(input_file)
        self._validate_key_labels()

    def _read_json_file(self, input_file: str) -> str:
        try:
            with open(input_file, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as json_error:
            # file is not found
            raise VaccineManagementException(self._error_message_json_not_found) from json_error
        except json.JSONDecodeError as json_error:
            raise VaccineManagementException(self._error_message_json_decode) from json_error
        return data

    def _validate_key_labels(self):
        i = 0
        for key in self._key_list:
            if not key in self._json_content.keys():
                raise VaccineManagementException(self._key_error_message[i])
            i = i + 1

    @property
    def json_content(self) -> str:
        """Funcion que devuelve el contenido"""
        return self._json_content
