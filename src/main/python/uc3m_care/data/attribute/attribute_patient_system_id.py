"""Clase para la validacion de patient_system_id"""
from uc3m_care.data.attribute.attribute import Attribute


class PatientSystemID(Attribute):
    """Clase para la validacion de patient_system_id"""
    def __init__(self, attr_value):
        self._validation_pattern = r"[0-9a-fA-F]{32}$"
        self._error_message = "patient system id is not valid"
        self._attr_value = self._validate(attr_value)
