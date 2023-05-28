"""Clase que validara todos los atributos"""
import re
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException


class Attribute:
    """Clase padre para la validacion de atributos"""
    def __init__(self):
        self._attr_value = ""
        self._validation_pattern = r""
        self._error_message = ""

    def _validate(self, attr_value: str) -> str:
        pattern = re.compile(self._validation_pattern)
        result = pattern.fullmatch(attr_value)
        if not result:
            raise VaccineManagementException(self._error_message)
        return attr_value

    @property
    def value(self) -> str:
        """Valor de el elemento a validar"""
        return self._attr_value

    @value.setter
    def value(self, attr_value: str):
        self._attr_value = attr_value
