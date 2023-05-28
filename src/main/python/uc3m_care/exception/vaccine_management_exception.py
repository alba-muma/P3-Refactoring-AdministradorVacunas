"""Exception for the access_management module"""

class VaccineManagementException(Exception):
    """Personalised exception for Vaccine Management"""
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self) -> str:
        """gets the message value"""
        return self.__message

    @message.setter
    def message(self, param_message: str):
        self.__message = param_message
