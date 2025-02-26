import unittest
from src.models.part import Part


class TestPart(unittest.TestCase):
    __manufacturer = 'Corsair'
    __name = 'VENGEANCE Series 16GB (1x16GB) DDR4 3200MHz C22 SODIMM Laptop Memory - Black'
    __sku = 6519625
    __price = 25.99

    def setUp(self):
        self.__part = Part(self.__manufacturer, self.__name, self.__sku, self.__price)

    def test_get_manufacturer(self):
        self.assertEqual(self.__part.get_manufacturer(), self.__manufacturer)

    def test_get_name(self):
        self.assertEqual(self.__part.get_name(), self.__name)

    def test_get_sku(self):
        self.assertEqual(self.__part.get_sku(), self.__sku)

    def test_get_price(self):
        self.assertEqual(self.__part.get_price(), self.__price)

    def test_set_manufacturer(self):
        self.__part.set_manufacturer('Test Manufacturer')
        self.assertEqual(self.__part.get_manufacturer(), 'Test Manufacturer')

    def test_set_name(self):
        self.__part.set_name('Test Name')
        self.assertEqual(self.__part.get_name(), 'Test Name')

    def test_set_sku(self):
        self.__part.set_sku(123456)
        self.assertEqual(self.__part.get_sku(), 123456)

    def test_set_price(self):
        self.__part.set_price(49.99)
        self.assertEqual(self.__part.get_price(), 49.99)
