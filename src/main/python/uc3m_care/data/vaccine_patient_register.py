"""MODULE: access_request. Contains the access request class"""
import hashlib
import json
from datetime import datetime
from freezegun import freeze_time
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException
from uc3m_care.data.attribute.attribute_registration_type import RegistrationType
from uc3m_care.data.attribute.attribute_phone_number import PhoneNumber
from uc3m_care.data.attribute.attribute_uuid import Uuid
from uc3m_care.data.attribute.attribute_name_surname import NameSurname
from uc3m_care.data.attribute.attribute_age import Age


class VaccinePatientRegister:
    """Class representing the register of the patient in the system"""
    _key_patient_id = "_VaccinePatientRegister__patient_id"
    _key_phone = "_VaccinePatientRegister__phone_number"
    _key_name = "_VaccinePatientRegister__full_name"
    _key_registration_type = "_VaccinePatientRegister__registration_type"
    _key_age = "_VaccinePatientRegister__age"
    _key_time_stamp = "_VaccinePatientRegister__time_stamp"
    _message_error = "Patient's data have been manipulated"
    # pylint: disable=too-many-arguments
    def __init__(self, patient_id, full_name, registration_type, phone_number, age) -> None:

        self.__patient_id = Uuid(patient_id).value
        self.__full_name = NameSurname(full_name).value
        self.__registration_type = RegistrationType(registration_type).value
        self.__phone_number = PhoneNumber(phone_number).value
        self.__age = Age(age).value
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)
        self.__patient_sys_id = hashlib.md5(self.__str__().encode()).hexdigest()

    def __str__(self) -> str:
        return "VaccinePatientRegister:" + json.dumps(self.__dict__)

    @property
    def full_name(self) -> str:
        """Property representing the name and the surname of
        the person who request the registration"""
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name_param: str):
        self.__full_name = NameSurname(full_name_param).value

    @property
    def vaccine_type(self) -> str:
        """Property representing the type vaccine"""
        return self.__registration_type

    @vaccine_type.setter
    def vaccine_type(self, vaccine_type_param: str):
        self.__registration_type = RegistrationType(vaccine_type_param).value

    @property
    def phone_number(self) -> str:
        """Property representing the requester's phone number"""
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number_param: str):
        self.__phone_number = PhoneNumber(phone_number_param).value

    @property
    def patient_id(self) -> str:
        """Property representing the requester's UUID"""
        return self.__patient_id

    @patient_id.setter
    def patient_id(self, patient_id_param: str):
        self.__patient_id = Uuid(patient_id_param).value

    @property
    def time_stamp(self) -> float:
        """Read-only property that returns the timestamp of the request"""
        return self.__time_stamp

    @property
    def patient_system_id(self) -> str:
        """Returns the md5 signature"""
        return self.__patient_sys_id

    @property
    def age(self) -> str:
        """Returns the patient's age"""
        return self.__age

    @age.setter
    def age(self, age_param: str):
        self.__age = Age(age_param).value

    @property
    def patient_sys_id(self) -> str:
        """Property representing the md5 generated"""
        return self.__patient_sys_id

    @classmethod
    def check_patient_sys_id(cls, patient_system_id: dict, paciente: dict) -> str:
        """Comprueba que los elementos del paciente encontrado sean correctos"""
        guid = paciente[cls._key_patient_id]
        name = paciente[cls._key_name]
        reg_type = paciente[cls._key_registration_type]
        phone = paciente[cls._key_phone]
        age = paciente[cls._key_age]
        # set the date when the patient was registered for checking the md5
        patient_timestamp = paciente[cls._key_time_stamp]
        freezer = freeze_time(datetime.fromtimestamp(patient_timestamp).date())
        freezer.start()
        patient = cls(guid, name, reg_type, phone, age)
        freezer.stop()
        if patient.patient_system_id != patient_system_id:
            raise VaccineManagementException(cls._message_error)
        return guid
