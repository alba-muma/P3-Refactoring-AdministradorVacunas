"""Clase hija de jsonStore para el json patient"""
from uc3m_care.data.vaccine_patient_register import VaccinePatientRegister
from uc3m_care.cfg.vaccine_manager_config import JSON_FILES_PATH
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException
from uc3m_care.storage.json_store import JsonStore

class PatientJsonStore(JsonStore):
    """Clase para el json patient"""
    _ID_FIELD = "_VaccinePatientRegister__patient_id"
    _ID_FIELD2 = "_VaccinePatientRegister__patient_sys_id"
    _FILE_PATH = JSON_FILES_PATH + "store_patient.json"
    def __init__(self):
        pass

    def save_store(self, data: VaccinePatientRegister) -> True:
        """Medthod for savint the patients store"""
        data_list = self.load_store()

        found = False
        item_found = self.find_store(data.patient_id)
        if item_found is not None:
            if (item_found["_VaccinePatientRegister__registration_type"] == data.vaccine_type) and \
                    (item_found["_VaccinePatientRegister__full_name"] == data.full_name):
                found = True

        if found is False:
            data_list.append(data.__dict__)

        self.write_store(data_list)

        if found is True:
            raise VaccineManagementException("patien_id is registered in store_patient")
        return True

    def find_patient_store(self, data: dict) -> VaccinePatientRegister:
        """Busca un paciente en la tienda"""
        item_found = self.find_store(data["PatientSystemID"], self._ID_FIELD2)
        return item_found

