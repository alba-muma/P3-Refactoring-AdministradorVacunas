"""Clase hija de jsonStore para el json appointment"""

from uc3m_care.cfg.vaccine_manager_config import JSON_FILES_PATH
from uc3m_care.storage.json_store import JsonStore

class AppointmentJsonStore(JsonStore):
    """Clase para el json appointment"""
    class __AppointmentJsonStore(JsonStore):
        """Patron singleton"""
        _FILE_PATH = JSON_FILES_PATH + "store_date.json"
        _ID_FIELD = "_VaccinationAppoinment__date_signature"
        def __init__(self):
            pass

        def find_date_signature(self, date_signature):
            """Busca date_signature"""
            self.check_store()
            return self.find_store(date_signature)

        def check_store(self):
            """Devuelve la lista de elementos de un json"""
            date_list = self.load_store(debe_existir_json=True)
            return date_list

    __instance = None

    def __new__(cls):
        if not AppointmentJsonStore.__instance:
            AppointmentJsonStore.__instance = AppointmentJsonStore.__AppointmentJsonStore()
        return AppointmentJsonStore.__instance

