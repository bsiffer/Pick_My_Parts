import unittest
from django.test import TestCase
from apps.core.models.ram import RAM
from apps.core.models.motherboard import Motherboard
from apps.core.models.cpu import CPU
from apps.core.models.parts_list import PartsList


class TestRAM(TestCase):
    def setUp(self):
        # create a sample RAM module
        self.ram = RAM.objects.create(
            manufacturer="Corsair",
            name="Vengeance LPX 16GB",
            sku=500001,
            price=79.99,
            capacity_in_gb=16,
            ddr_standard="DDR4",
            speed_in_mhz=3200,
            sticks=2,
            latency="CL16",
            rgb=False,
            color="Black"
        )
        # create a sample motherboard that supports DDR4 with 4 slots
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
        # create a sample CPU where DDR4 is supported
        self.cpu = CPU.objects.create(
            manufacturer="AMD",
            name="Ryzen 5 5600X",
            sku=100010,
            price=299.99,
            architecture="Zen 3",
            clock_speed=3.7,
            ddr4_compatibility=True,
            ddr5_compatibility=False,
            socket_type="AM4",
            wattage_compatibility=65.0,
            bios_compatibility="UEFI",
            chipset_compatibility="B550"
        )
        # create a PartsList instance and add a motherboard and CPU.
        self.parts_list = PartsList()
        self.parts_list.parts["Motherboard"] = [self.motherboard]
        self.parts_list.parts["CPU"] = [self.cpu]

    def test_initialization(self):
        # Verify the RAM attributes
        self.assertEqual(self.ram.manufacturer, "Corsair")
        self.assertEqual(self.ram.name, "Vengeance LPX 16GB")
        self.assertEqual(self.ram.sku, 500001)
        self.assertAlmostEqual(float(self.ram.price), 79.99)
        self.assertEqual(self.ram.capacity_in_gb, 16)
        self.assertEqual(self.ram.ddr_standard, "DDR4")
        self.assertEqual(self.ram.speed_in_mhz, 3200)
        self.assertEqual(self.ram.sticks, 2)
        self.assertEqual(self.ram.latency, "CL16")
        self.assertFalse(self.ram.rgb)
        self.assertEqual(self.ram.color, "Black")

    def test_string_representation(self):
        expected_str = (
            f"Manufacturer: {self.ram.manufacturer}\n"
            f"Name: {self.ram.name}\n"
            f"SKU: {self.ram.sku}\n"
            f"Price: ${self.ram.price:.2f}"
            f"\nCapacity: {self.ram.capacity_in_gb}GB\n"
            f"DDR Standard: {self.ram.ddr_standard}\n"
            f"Speed: {self.ram.speed_in_mhz}MHz\n"
            f"Sticks: {self.ram.sticks}\n"
            f"CAS Latency: {self.ram.latency}\n"
            f"RGB: {'Yes' if self.ram.rgb else 'No'}\n"
            f"Color: {self.ram.color}"
        )
        self.assertEqual(str(self.ram), expected_str)

    def test_check_compatibility_success(self):
        # when the RAM's DDR standard matches the motherboard's supported type
        issues = self.ram.check_compatibility(self.parts_list)
        self.assertEqual(issues, [])

    def test_check_compatibility_failure_due_to_ram_type(self):
        # create a new motherboard that only supports DDR3 (mismatch) for testing
        incompatible_mb = Motherboard.objects.create(
            manufacturer="TestMB",
            name="Incompatible MB",
            sku=654322,
            price=199.99,
            socket_type="AM4",
            form_factor="ATX",
            ram_slots=4,
            supported_ram_type="DDR3",  # Mismatch here
            chipset_compatibility="B550",
            bios_compatibility="UEFI",
            supported_storage_interfaces=["SATA III"],
            supported_pcie_standards=["PCIe 4.0"]
        )
        self.parts_list.parts["Motherboard"] = [incompatible_mb]
        issues = self.ram.check_compatibility(self.parts_list)
        # expect an issue about DDR standard mismatch
        self.assertTrue(any("incompatible" in issue.lower() and "DDR" in issue for issue in issues))


if __name__ == '__main__':
    unittest.main(verbosity=2)
