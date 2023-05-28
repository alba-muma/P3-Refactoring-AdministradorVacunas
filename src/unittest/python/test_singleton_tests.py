
"""Clase que invocara la clase AppointmentJsonStore y hara una comprobacion para su correcto funcionamiento"""

import unittest
from uc3m_care.storage.appointment_json_store import AppointmentJsonStore


class SingletonTests(unittest.TestCase):
    """Clase que invocara la clase AppointmentJsonStore y hara una comprobacion para
    su correcto funcionamiento"""
    def test_singleton_appointment_store(self):
        """Test que verifica el correcto funcionamiento de la clase"""

        mystore1 = AppointmentJsonStore()
        mystore2 = AppointmentJsonStore()
        mystore3 = AppointmentJsonStore()
        mystore4 = AppointmentJsonStore()

        self.assertEqual(mystore1, mystore2)
        self.assertEqual(mystore1, mystore3)
        self.assertEqual(mystore1, mystore4)


if __name__ == '__main__':
    unittest.main()
