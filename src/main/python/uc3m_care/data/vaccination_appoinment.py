"""Contains the class Vaccination Appoinment"""

import hashlib
from datetime import datetime
from uc3m_care.data.vaccine_log import VaccineLog
from uc3m_care.parser.appointment_json_parser import AppointmentJsonParser
from uc3m_care.data.attribute.attribute_patient_system_id import PatientSystemID
from uc3m_care.data.attribute.attribute_phone_number import PhoneNumber
from uc3m_care.data.vaccine_patient_register import VaccinePatientRegister
from uc3m_care.storage.patient_json_store import PatientJsonStore


# pylint: disable=too-many-instance-attributes
class VaccinationAppoinment:
    """Class representing an appoinment  for the vaccination of a patient"""
    _phone_key = "ContactPhoneNumber"
    _sys_id_key = "PatientSystemID"

    def __init__(self, input_file):
        self.__json_content = AppointmentJsonParser(input_file).json_content
        self.__alg = "SHA-256"
        self.__type = "DS"
        self.__patient_sys_id = PatientSystemID(self.__json_content[self._sys_id_key]).value
        self.__phone_number = PhoneNumber(self.__json_content[self._phone_key]).value
        my_store = PatientJsonStore()
        paciente = my_store.find_patient_store(self.__json_content)
        sys_id = self.__json_content[self._sys_id_key]
        uuid = VaccinePatientRegister.check_patient_sys_id(sys_id, paciente)
        self.__patient_id = uuid
        justnow = datetime.utcnow()
        self.__issued_at = datetime.timestamp(justnow)
        days = 10
        if days == 0:
            self.__appoinment_date = 0
        else:
            # timestamp is represneted in seconds.microseconds
            # age must be expressed in senconds to be added to the timestap
            self.__appoinment_date = self.__issued_at + (days * 24 * 60 * 60)
        date_signature = self.vaccination_signature
        self.__date_signature = date_signature

    def __signature_string(self) -> str:
        """Composes the string to be used for generating the key for the date"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",patient_sys_id:" + \
               self.__patient_sys_id + ",issuedate:" + self.__issued_at.__str__() + \
               ",vaccinationtiondate:" + self.__appoinment_date.__str__() + "}"

    @property
    def patient_id(self) -> str:
        """Property that represents the guid of the patient"""
        return self.__patient_id

    @patient_id.setter
    def patient_id(self, patient_id_param: str):
        self.__patient_id = patient_id_param

    @property
    def patient_sys_id(self) -> str:
        """Property that represents the patient_sys_id of the patient"""
        return self.__patient_sys_id

    @patient_sys_id.setter
    def patient_sys_id(self, date_signature: str):
        self.__patient_sys_id = VaccineLog.validate_date_signature(date_signature)

    @property
    def phone_number(self) -> str:
        """Property that represents the phone number of the patient"""
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number_param: str):
        self.__phone_number = phone_number_param

    @property
    def vaccination_signature(self) -> str:
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def issued_at(self) -> float:
        """Returns the issued at value"""
        return self.__issued_at

    @issued_at.setter
    def issued_at(self, issued_at_param: float):
        self.__issued_at = issued_at_param

    @property
    def appoinment_date(self) -> float:
        """Returns the vaccination date"""
        return self.__appoinment_date

    @property
    def date_signature(self) -> str:
        """Returns the SHA256 """
        return self.__date_signature
