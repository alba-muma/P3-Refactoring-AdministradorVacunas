"""Clase con las key y los errores para el json de appoinment"""
from uc3m_care.parser.json_parser import JsonParser

class AppointmentJsonParser(JsonParser):
    """Clase con las key y los errores para el json de appoinment"""
    _key_list = ["PatientSystemID", "ContactPhoneNumber"]
    _key_error_message = ["Bad label patient_id","Bad label contact phone"]
