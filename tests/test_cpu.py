import unittest
from src.models.cpu import CPU


class TestCPU(unittest.TestCase):
    __manufacturer = "AMD"
    __name = "AMD RYZEN 7 9800X3D"
    __sku = 566623
    __price = 339.99
    __architecture = "Zen 5"
    __clock_speed = 4.7
    __ddr4_compatibility = True
    __ddr5_compatibility = False
    __socket_type = "AM5"
    __wattage_compatibility = 105
    __bios_compatibility = "Yes"
    __chipset_compatibility = "Yes"

    def setUp(self):
        self.__cpu = CPU(
            self.__manufacturer,
            self.__name,
            self.__sku,
            self.__price,
            self.__architecture,
            self.__clock_speed,
            self.__ddr4_compatibility,
            self.__ddr5_compatibility,
            self.__socket_type,
            self.__wattage_compatibility,
            self.__bios_compatibility,
            self.__chipset_compatibility,
        )

    def test_get_architecture(self):
        self.assertEqual(self.__cpu.get_architecture(), self.__architecture)

    def test_get_clock_speed(self):
        self.assertEqual(self.__cpu.get_clock_speed(), self.__clock_speed)

    def test_get_ddr4_compatibility(self):
        self.assertEqual(self.__cpu.get_ddr4_compatibility(), self.__ddr4_compatibility)

    def test_get_ddr5_compatibility(self):
        self.assertEqual(self.__cpu.get_ddr5_compatibility(), self.__ddr5_compatibility)

    def test_get_socket_type(self):
        self.assertEqual(self.__cpu.get_socket_type(), self.__socket_type)

    def test_get_wattage_compatibility(self):
        self.assertEqual(
            self.__cpu.get_wattage_compatibility(), self.__wattage_compatibility
        )

    def test_get_bios_compatibility(self):
        self.assertEqual(self.__cpu.get_bios_compatibility(), self.__bios_compatibility)

    def test_get_chipset_compatibility(self):
        self.assertEqual(
            self.__cpu.get_chipset_compatibility(), self.__chipset_compatibility
        )

    def test_set_architecture(self):
        self.__cpu.set_architecture("Zen 3")
        self.assertEqual(self.__cpu.get_architecture(), "Zen 3")

    def test_set_clock_speed(self):
        self.__cpu.set_clock_speed(4.2)
        self.assertEqual(self.__cpu.get_clock_speed(), 4.2)

    def test_set_ddr4_compatibility(self):
        self.__cpu.set_ddr4_compatibility(False)
        self.assertEqual(self.__cpu.get_ddr4_compatibility(), False)

    def test_set_ddr5_compatibility(self):
        self.__cpu.set_ddr5_compatibility(True)
        self.assertEqual(self.__cpu.get_ddr5_compatibility(), True)

    def test_set_socket_type(self):
        self.__cpu.set_socket_type("AM4")
        self.assertEqual(self.__cpu.get_socket_type(), "AM4")

    def test_set_wattage_compatibility(self):
        self.__cpu.set_wattage_compatibility(95)
        self.assertEqual(self.__cpu.get_wattage_compatibility(), 95)

    def test_set_bios_compatibility(self):
        self.__cpu.set_bios_compatibility("No")
        self.assertEqual(self.__cpu.get_bios_compatibility(), "No")

    def test_set_chipset_compatibility(self):
        self.__cpu.set_chipset_compatibility("No")
        self.assertEqual(self.__cpu.get_chipset_compatibility(), "No")

    def test_to_string(self):
        expected_output = (
            f"Part Name: {self.__name}\nPrice: {self.__price}\nSKU: {self.__sku}\nManufacturer: {self.__manufacturer}\n"
            f"Architecture: {self.__architecture}\nClock Speed: {self.__clock_speed}\n"
        )
        self.assertEqual(self.__cpu.to_string(), expected_output)


if __name__ == "__main__":
    unittest.main()
