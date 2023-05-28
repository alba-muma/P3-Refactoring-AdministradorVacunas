"""Se crea la clase de almacen para archivos json """
import json
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException

class JsonStore():
    """Calse para el almacen de archivos json"""
    _FILE_PATH = ""
    _ID_FIELD = ""
    _message_error_format = "JSON Decode Error - Wrong JSON Format"
    _message_error_not_found = "Store_date not found"
    _message_error_path = "Wrong file or file path"
    def __init__(self):
        pass

    def find_store(self, item_to_find, id_field=None):
        """Funcion que busca un item"""
        data_list = self.load_store()
        if not id_field:
            id_field = self._ID_FIELD
        for item in data_list:
            if item[id_field] == item_to_find:
                return item
        return None

    def write_store(self, data_list):
        """Funcion que abre un archivo para escribir en el"""
        try:
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as json_error:
            raise VaccineManagementException(self._message_error_path) from json_error

    def load_store(self, debe_existir_json=False):
        """Funcion que carga la tienda"""
        try:
            with open(self._FILE_PATH, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError as json_error:
            if debe_existir_json:
                raise VaccineManagementException(self._message_error_not_found) from json_error
            data_list = []
        except json.JSONDecodeError as json_error:
            raise VaccineManagementException(self._message_error_format) from json_error
        return data_list

    def add_item(self, date):
        """Añade un item en un json"""
        data_list = self.load_store()
        # append the date
        data_list.append(date.__dict__)
        self.write_store(data_list)
