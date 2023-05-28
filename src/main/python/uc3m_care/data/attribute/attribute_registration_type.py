"""Clase para la validacion de registration type"""
from uc3m_care.data.attribute.attribute import Attribute


class RegistrationType(Attribute):
    """Clase para la validacion de registration type"""
    def __init__(self, attr_value):
        self._validation_pattern = r"(Regular|Family)"
        self._error_message = "Registration type is nor valid"
        self._attr_value = self._validate(attr_value)

