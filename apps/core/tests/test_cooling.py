import unittest
from apps.core.models.cooling import CoolingAccessory


class TestCoolingAccessory(unittest.TestCase):
    def setUp(self):
        self.__cooling_accessory = CoolingAccessory("A", "B", 12345, 12.99, "Liquid")

    def test_get_cooling_type(self):
        self.assertEqual("Liquid", self.__cooling_accessory.get_cooling_type())

