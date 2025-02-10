import unittest
from src.models.motherboard import Motherboard

class TestMotherboard(unittest.TestCase):
    __manufacturer = "ASUS"
    __name = "ROG STRIX B550-F Gaming"
    __sku = 1234567
    __price = 189.99
    __architecture = "x86-64"
    __standard_size = "ATX"
    __ram_slots = 4
    __compatibility = ["AMD Ryzen 3000 Series", "AMD Ryzen 5000 Series"]

    def setUp(self):
        self.__motherboard = Motherboard(
            self.__manufacturer, self.__name, self.__sku, self.__price,
            self.__architecture, self.__standard_size, self.__ram_slots, self.__compatibility
        )

    def test_get_manufacturer(self):
        self.assertEqual(self.__motherboard.get_manufacturer(), self.__manufacturer)

    def test_get_name(self):
        self.assertEqual(self.__motherboard.get_name(), self.__name)

    def test_get_sku(self):
        self.assertEqual(self.__motherboard.get_sku(), self.__sku)

    def test_get_price(self):
        self.assertEqual(self.__motherboard.get_price(), self.__price)

    def test_display_info(self):
        expected_output = (f"Part Name: {self.__name}\nPrice: {self.__price}\n "
                           f"SKU: {self.__sku}\nManufacturer: {self.__manufacturer}\n"
                           f"Architecture: {self.__architecture}, Size: {self.__standard_size}, "
                           f"RAM Slots: {self.__ram_slots}, Compatibility: {self.__compatibility}")
        self.assertEqual(self.__motherboard.display_info(), expected_output)

if __name__ == '__main__':
    unittest.main()
