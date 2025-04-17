import unittest
from django.test import TestCase
from apps.core.models.motherboard import Motherboard


class TestMotherboard(TestCase):
    def setUp(self):
        self.motherboard = Motherboard.objects.create(
            manufacturer="ASUS",
            name="ROG Strix B550-F",
            sku=654321,
            price=179.99,
            socket_type="AM4",
            form_factor="ATX",
            ram_slots=4,
            supported_ram_type="DDR4",
            chipset_compatibility="B550",
            bios_compatibility="UEFI",
            supported_storage_interfaces=["SATA III", "NVMe SSD"],
            supported_pcie_standards=["PCIe 4.0", "PCIe 3.0"]
        )

    def test_initialization(self):
        # Verify that the motherboard is created with the correct attributes.
        self.assertEqual(self.motherboard.manufacturer, "ASUS")
        self.assertEqual(self.motherboard.name, "ROG Strix B550-F")
        self.assertEqual(self.motherboard.sku, 654321)
        self.assertAlmostEqual(float(self.motherboard.price), 179.99)
        self.assertEqual(self.motherboard.socket_type, "AM4")
        self.assertEqual(self.motherboard.form_factor, "ATX")
        self.assertEqual(self.motherboard.ram_slots, 4)
        self.assertEqual(self.motherboard.supported_ram_type, "DDR4")
        self.assertEqual(self.motherboard.chipset_compatibility, "B550")
        self.assertEqual(self.motherboard.bios_compatibility, "UEFI")
        self.assertEqual(self.motherboard.supported_storage_interfaces, ["SATA III", "NVMe SSD"])
        self.assertEqual(self.motherboard.supported_pcie_standards, ["PCIe 4.0", "PCIe 3.0"])

    def test_string_representation(self):
        # Build the expected string representation.
        expected_str = (
            f"Manufacturer: {self.motherboard.manufacturer}\n"
            f"Name: {self.motherboard.name}\n"
            f"SKU: {self.motherboard.sku}\n"
            f"Price: ${self.motherboard.price:.2f}"
            f"\nSocket Type: {self.motherboard.socket_type}, Form Factor: {self.motherboard.form_factor}, "
            f"RAM Slots: {self.motherboard.ram_slots}, Supported RAM Type: {self.motherboard.supported_ram_type}"
        )
        self.assertEqual(str(self.motherboard), expected_str)


if __name__ == '__main__':
    # Using verbosity=2 provides detailed output when running the test directly.
    unittest.main(verbosity=2)
