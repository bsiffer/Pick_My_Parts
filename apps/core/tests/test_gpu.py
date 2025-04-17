import unittest
from django.test import TestCase
from apps.core.models.gpu import GPU
from apps.core.models.motherboard import Motherboard
from apps.core.models.parts_list import PartsList


class TestGPU(TestCase):
    def setUp(self):
        # Create a GPU instance.
        self.gpu = GPU.objects.create(
            manufacturer="NVIDIA",
            name="RTX 3080",
            sku=200001,
            price=699.99,
            architecture="Ampere",
            memory_bus=320,
            pcie_standard="PCIe 4.0",
            slot_size="2-Slot",
            length_in_mm=285.0,
            cooling_type="Air Cooler",
            power_requirement=320.0,
            power_connectors="2x8-pin",
            color="Black"
        )

        # Create a compatible motherboard that supports PCIe 4.0.
        self.compatible_mb = Motherboard.objects.create(
            manufacturer="ASUS",
            name="ROG STRIX Z690-E",
            sku=300001,
            price=399.99,
            socket_type="LGA1700",
            form_factor="ATX",
            ram_slots=4,
            supported_ram_type="DDR5",
            chipset_compatibility="Z690",
            bios_compatibility="UEFI",
            supported_storage_interfaces=["NVMe SSD", "SATA III"],
            supported_pcie_standards=["PCIe 4.0", "PCIe 3.0"]
        )

        # Create an incompatible motherboard that does not support PCIe 4.0.
        self.incompatible_mb = Motherboard.objects.create(
            manufacturer="MSI",
            name="MPG B550 Gaming Edge",
            sku=300002,
            price=179.99,
            socket_type="AM4",
            form_factor="ATX",
            ram_slots=4,
            supported_ram_type="DDR4",
            chipset_compatibility="B550",
            bios_compatibility="UEFI",
            supported_storage_interfaces=["SATA III"],
            supported_pcie_standards=["PCIe 3.0"]  # Lacks PCIe 4.0
        )

        # Create a PartsList instance.
        self.parts_list = PartsList()

    def test_initialization(self):
        self.assertEqual(self.gpu.manufacturer, "NVIDIA")
        self.assertEqual(self.gpu.name, "RTX 3080")
        self.assertEqual(self.gpu.sku, 200001)
        self.assertAlmostEqual(float(self.gpu.price), 699.99)
        self.assertEqual(self.gpu.architecture, "Ampere")
        self.assertEqual(self.gpu.memory_bus, 320)
        self.assertEqual(self.gpu.pcie_standard, "PCIe 4.0")
        self.assertEqual(self.gpu.slot_size, "2-Slot")
        self.assertAlmostEqual(float(self.gpu.length_in_mm), 285.0)
        self.assertEqual(self.gpu.cooling_type, "Air Cooler")
        self.assertAlmostEqual(float(self.gpu.power_requirement), 320.0)
        self.assertEqual(self.gpu.power_connectors, "2x8-pin")
        self.assertEqual(self.gpu.color, "Black")

    def test_string_representation(self):
        expected_str = (
            f"Manufacturer: {self.gpu.manufacturer}\n"
            f"Name: {self.gpu.name}\n"
            f"SKU: {self.gpu.sku}\n"
            f"Price: ${self.gpu.price:.2f}\n"
            f"Architecture: {self.gpu.architecture}\n"
            f"Memory Bus: {self.gpu.memory_bus}-bit\n"
            f"PCIe Standard: {self.gpu.pcie_standard}\n"
            f"Slot Size: {self.gpu.slot_size}\n"
            f"Length: {self.gpu.length_in_mm}mm\n"
            f"Cooling Type: {self.gpu.cooling_type}\n"
            f"Power Requirement: {self.gpu.power_requirement}W\n"
            f"Power Connectors: {self.gpu.power_connectors}\n"
            f"Color: {self.gpu.color}"
        )
        self.assertEqual(str(self.gpu), expected_str)

    def test_check_compatibility_success(self):
        # Add a compatible motherboard to the PartsList.
        self.parts_list.parts["Motherboard"] = [self.compatible_mb]
        issues = self.gpu.check_compatibility(self.parts_list)
        self.assertEqual(issues, [])

    def test_check_compatibility_failure(self):
        # Add an incompatible motherboard to the PartsList.
        self.parts_list.parts["Motherboard"] = [self.incompatible_mb]
        issues = self.gpu.check_compatibility(self.parts_list)
        # Verify that at least one incompatibility issue is reported.
        self.assertTrue(len(issues) > 0)
        for issue in issues:
            self.assertIn("not compatible", issue.lower())


if __name__ == '__main__':
    unittest.main(verbosity=2)
