from django.test import TestCase
from apps.core.models.cpu import CPU

class TestCoolingAccessory(TestCase):
    def setUp(self):
        self.cpu = CPU.objects.create(
            manufacturer="XYZ",
            name="XYZ CPU",
            sku=112233,
            price=49.99,
            architecture="Zen 5",
            clock_speed = 4.7,
            ddr4_compatibility = True,
            ddr5_compatibility = False,
            socket_type = 'AM5',
            wattage_compatibility = 105,
            bios_compatibility = True,
            chipset_compatibility = True,
        )

    def test_initialization(self):
        self.assertEqual(self.cpu.manufacturer, "XYZ")
        self.assertEqual(self.cpu.name, "XYZ CPU")
        self.assertEqual(self.cpu.sku, 112233)
        self.assertEqual(self.cpu.price, 49.99)

        self.assertEqual(self.cpu.architecture, "Zen 5")
        self.assertEqual(self.cpu.clock_speed, 4.7)
        self.assertEqual(self.cpu.ddr4_compatibility, True)
        self.assertEqual(self.cpu.ddr5_compatibility, False)
        self.assertEqual(self.cpu.socket_type, 'AM5')
        self.assertEqual(self.cpu.wattage_compatibility, 105)
        self.assertEqual(self.cpu.bios_compatibility, True)
        self.assertEqual(self.cpu.chipset_compatibility, True)

    def test_string_representation(self):
        expected_str = (
            f"Manufacturer: {self.cpu.manufacturer}\n"
            f"Name: {self.cpu.name}\n"
            f"SKU: {self.cpu.sku}\n"
            f"Price: ${self.cpu.price:.2f}"
            f"\nArchitecture: {self.cpu.architecture}"
            f"\nClock Speed: {self.cpu.clock_speed}"
            f"\nDDR4 Compatibility = {self.cpu.ddr4_compatibility}"
            f"\nDDR5 Compatibility = {self.cpu.ddr5_compatibility}"
            f"\nSocket Type = {self.cpu.socket_type}"
            f"\nWattage Compatibility = {self.cpu.wattage_compatibility}"
            f"\nBIOS Compatibility = {self.cpu.bios_compatibility}"
            f"\nChipset Compatibility = {self.cpu.chipset_compatibility}"
        )
        self.assertEqual(str(self.cpu), expected_str)
