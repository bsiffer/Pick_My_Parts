from django.test import TestCase
from apps.core.models.cpu import CPU
from apps.core.models.motherboard import Motherboard
from apps.core.models.parts_list import PartsList


class TestCPU(TestCase):
    def setUp(self):
        # Create a CPU instance.
        self.cpu = CPU.objects.create(
            name="Intel Core i9-13900K",
            manufacturer="Intel",
            sku=112233,
            price=49.99,
            architecture="Raptor Lake",
            clock_speed=5.80,
            ddr4_compatibility=True,
            ddr5_compatibility=True,
            socket_type="LGA 1700",
            wattage_compatibility=125.0,
            bios_compatibility='UEFI',
            chipset_compatibility='B550'
        )

        # Create a compatible motherboard (matches socket, BIOS, and chipset).
        self.compatible_motherboard = Motherboard.objects.create(
            name="Compatible MB",
            manufacturer="ASUS",
            sku=654321,
            price=179.99,
            socket_type="LGA 1700",
            form_factor="ATX",
            ram_slots=4,
            supported_ram_type="DDR4",
            chipset_compatibility='B550',
            bios_compatibility='UEFI',
            supported_storage_interfaces=[],
            supported_pcie_standards=[]
        )

        # Create an incompatible motherboard (mismatched socket, chipset, and BIOS).
        self.incompatible_motherboard = Motherboard.objects.create(
            name="Incompatible MB",
            manufacturer="ASUS",
            sku=654322,
            price=199.99,
            socket_type="AM4",
            form_factor="ATX",
            ram_slots=4,
            supported_ram_type="DDR4",
            chipset_compatibility='X570',
            bios_compatibility='Legacy',
            supported_storage_interfaces=[],
            supported_pcie_standards=[]
        )

        # Create a parts list instance.
        self.parts_list = PartsList()

    def test_initialization(self):
        # Test that the CPU instance is set up correctly.
        self.assertEqual(self.cpu.manufacturer, "Intel")
        self.assertEqual(self.cpu.name, "Intel Core i9-13900K")
        self.assertEqual(self.cpu.sku, 112233)
        self.assertAlmostEqual(float(self.cpu.price), 49.99)
        self.assertEqual(self.cpu.architecture, "Raptor Lake")
        self.assertAlmostEqual(float(self.cpu.clock_speed), 5.8)
        self.assertTrue(self.cpu.ddr4_compatibility)
        self.assertTrue(self.cpu.ddr5_compatibility)
        self.assertEqual(self.cpu.socket_type, 'LGA 1700')
        self.assertAlmostEqual(float(self.cpu.wattage_compatibility), 125.0)
        self.assertEqual(self.cpu.bios_compatibility, 'UEFI')
        self.assertEqual(self.cpu.chipset_compatibility, 'B550')

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

    def test_check_compatibility_with_compatible_motherboard(self):
        # Add a compatible motherboard to the parts list.
        self.parts_list.parts["Motherboard"] = [self.compatible_motherboard]
        # Test the CPU compatibility: Expect an empty issues list.
        issues = self.cpu.check_compatibility(self.parts_list)
        self.assertEqual(issues, [])

    def test_check_compatibility_with_incompatible_motherboard(self):
        # Add an incompatible motherboard to the parts list.
        self.parts_list.parts["Motherboard"] = [self.incompatible_motherboard]
        # Test the CPU compatibility: Expect one or more issues.
        issues = self.cpu.check_compatibility(self.parts_list)
        self.assertTrue(len(issues) >= 1)
        for issue in issues:
            self.assertIn("not compatible", issue)


if __name__ == '__main__':
    import unittest

    unittest.main()
