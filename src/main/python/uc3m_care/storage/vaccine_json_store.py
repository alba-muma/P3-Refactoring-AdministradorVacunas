"""Clase hija de jsonStore para el json vaccine"""
from uc3m_care.cfg.vaccine_manager_config import JSON_FILES_PATH
from uc3m_care.storage.json_store import JsonStore


class VaccineJsonStore(JsonStore):
    """Clase para el json vaccine"""
    _FILE_PATH = JSON_FILES_PATH + "store_vaccine.json"
    _ID_FIELD = ""
    def __init__(self):
        pass
