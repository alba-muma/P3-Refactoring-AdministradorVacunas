"""Clase para validar los elemento de la vacuna"""

import re
from datetime import datetime
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException
from uc3m_care.storage.appointment_json_store import AppointmentJsonStore


class VaccineLog:
    """Clase para validar los elemento de la vacuna"""
    _error_message_datesig_notvalid = "date_signature format is not valid"
    _error_message_datesig_notfound = "date_signature is not found"
    _error_message_date = "Today is not the date"
    _pattern = r"[0-9a-fA-F]{64}$"
    _key_appointment_date = "_VaccinationAppoinment__appoinment_date"

    def __init__(self, date_signature):
        self.__date_signature = self.validate_date_signature(date_signature)

    def validate_date_signature(self, date_signature: str) -> str:
        """Valida date signature"""
        pattern = re.compile(self._pattern)
        result = pattern.fullmatch(date_signature)
        if not result:
            raise VaccineManagementException(self._error_message_datesig_notvalid)
        return date_signature

    @property
    def date_signature(self) -> str:
        """date signature"""
        return self.__date_signature

    def check_date(self):
        """Comprueba la fecha"""
        date_found = self.check_the_date_signature()
        date_time = date_found[self._key_appointment_date]
        self.is_the_date(date_time)

    def check_the_date_signature(self):
        """Comprueba date_signature"""
        # check if this date is in store_date
        my_store_date = AppointmentJsonStore()
        date_found = my_store_date.find_date_signature(self.__date_signature)
        if not date_found:
            raise VaccineManagementException(self._error_message_datesig_notfound)
        return date_found

    def is_the_date(self, date_time: float):
        """Comprueba si la fecha es el dia de hoy"""
        today = datetime.today().date()
        date_patient = datetime.fromtimestamp(date_time).date()
        if date_patient != today:
            raise VaccineManagementException(self._error_message_date)
