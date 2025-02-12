import unittest
from src.models.cpu import cpu


class TestCPU(unittest.TestCase):
    __manufacturer = "AMD"
    __name = "AMD RYZEN 7 9800X3D"
    __sku = 566623
    __price = 339.99
    __architecture = "Zen 5"
    __clock_speed = 4.7

    def setUp(self):
        self.__cpu = cpu(
            self.__manufacturer,
            self.__name,
            self.__sku,
            self.__price,
            self.__architecture,
            self.__clock_speed,
        )

    def test_get_architecture(self):
        self.assertEqual(self.__cpu.get_architecture(), self.__architecture)

    def test_get_clock_speed(self):
        self.assertEqual(self.__cpu.get_clock_speed(), self.__clock_speed)

    def test_set_architecture(self):
        self.__cpu.set_architecture("Zen 3")
        self.assertEqual(self.__cpu.get_architecture(), "Zen 3")

    def test_set_clock_speed(self):
        self.__cpu.set_clock_speed(4.2)
        self.assertEqual(self.__cpu.get_clock_speed(), 4.2)

    def test_display_info(self):
        expected_output = (
            f"Part Name: {self.__name}\nPrice: {self.__price}\n "
            f"Architecture: {self.__architecture}\nClock Speed: {self.__clock_speed}\n"
        )
        self.assertEqual(self.__cpu.display_info(), expected_output)


if __name__ == "__main__":
    unittest.main()
