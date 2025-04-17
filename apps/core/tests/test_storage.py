import unittest
from django.test import TestCase
from apps.core.models.storage import Storage
from apps.core.models.motherboard import Motherboard
from apps.core.models.parts_list import PartsList


class TestStorage(TestCase):
    def setUp(self):
        # Create a Storage instance.
        self.storage = Storage.objects.create(
            manufacturer="Samsung",
            name="970 EVO Plus 1TB",
            sku=123450,
            price=129.99,
            storage_type="NVMe SSD",
            capacity_in_GB=1000,
            interface="PCIe 3.0 x4"
        )

        # Create a Motherboard instance that supports PCIe storage interface.
        self.motherboard = Motherboard.objects.create(
            manufacturer="ASUS",
            name="ROG Strix Z690-E",
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

        # Prepare a PartsList for compatibility testing.
        self.parts_list = PartsList()
        self.parts_list.parts["Motherboard"] = [self.motherboard]

    def test_initialization(self):
        # Verify that the storage instance is created correctly.
        self.assertEqual(self.storage.manufacturer, "Samsung")
        self.assertEqual(self.storage.name, "970 EVO Plus 1TB")
        self.assertEqual(self.storage.sku, 123450)
        self.assertAlmostEqual(float(self.storage.price), 129.99)
        self.assertEqual(self.storage.storage_type, "NVMe SSD")
        self.assertEqual(self.storage.capacity_in_GB, 1000)
        self.assertEqual(self.storage.interface, "PCIe 3.0 x4")

    def test_string_representation(self):
        expected_str = (
            f"Manufacturer: {self.storage.manufacturer}\n"
            f"Name: {self.storage.name}\n"
            f"SKU: {self.storage.sku}\n"
            f"Price: ${self.storage.price:.2f}\n"
            f"Type: {self.storage.storage_type}\n"
            f"Capacity: {self.storage.capacity_in_GB}GB\n"
            f"Interface: {self.storage.interface}"
        )
        self.assertEqual(str(self.storage), expected_str)

    def check_compatibility(self, parts_list):
        """
        Checks if this storage device is compatible with a motherboard in the parts list.
        Returns a list of issues (empty if compatible).
        """
        issues = []
        motherboards = parts_list.parts.get("Motherboard", [])

        if len(motherboards) == 1:
            # Assume only one motherboard is selected.
            motherboard = motherboards[0]
            # Use storage_type to compare with the motherboard's supported storage interfaces.
            if self.storage_type not in motherboard.supported_storage_interfaces:
                issues.append(
                    f"Storage '{self.get_name()}' with type '{self.storage_type}' is not supported by motherboard '{motherboard.get_name()}'."
                )
        else:
            issues.append("No motherboard selected.")

        return issues


if __name__ == '__main__':
    unittest.main(verbosity=2)
