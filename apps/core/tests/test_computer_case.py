import unittest
from django.test import TestCase
from apps.core.models.computer_case import ComputerCase
from apps.core.models.form_factor import FormFactor
from apps.core.models.motherboard import Motherboard
from apps.core.models.parts_list import PartsList


class TestComputerCase(TestCase):
    def setUp(self):
        # Create FormFactor instances for testing.
        self.atx, _ = FormFactor.objects.get_or_create(name="ATX")
        self.micro_atx, _ = FormFactor.objects.get_or_create(name="Micro-ATX")

        # Create a ComputerCase instance.
        self.computer_case = ComputerCase.objects.create(
            manufacturer="NZXT",
            name="H510",
            sku=123456,
            price=99.99,
            form_factor=self.atx,
            color="Black"
        )
        # Assume the case supports its own form factor and Micro-ATX.
        self.computer_case.supported_form_factors.set([self.atx, self.micro_atx])

        # Prepare a PartsList instance.
        self.parts_list = PartsList()

        # Create a compatible Motherboard with form factor 'ATX'
        self.compatible_mb = Motherboard.objects.create(
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

        # Create an incompatible Motherboard with form factor 'Mini-ITX'
        self.incompatible_mb = Motherboard.objects.create(
            manufacturer="Gigabyte",
            name="AORUS Mini",
            sku=654322,
            price=149.99,
            socket_type="AM4",
            form_factor="Mini-ITX",  # Incompatible with our case which supports ATX and Micro-ATX
            ram_slots=2,
            supported_ram_type="DDR4",
            chipset_compatibility="B450",
            bios_compatibility="UEFI",
            supported_storage_interfaces=["SATA III"],
            supported_pcie_standards=["PCIe 3.0"]
        )

    def test_initialization(self):
        # Verify that the ComputerCase instance is created with the correct attributes.
        self.assertEqual(self.computer_case.manufacturer, "NZXT")
        self.assertEqual(self.computer_case.name, "H510")
        self.assertEqual(self.computer_case.sku, 123456)
        self.assertAlmostEqual(float(self.computer_case.price), 99.99)
        self.assertEqual(self.computer_case.color, "Black")
        self.assertEqual(self.computer_case.form_factor, self.atx)
        # Check supported form factors.
        supported = [ff.name for ff in self.computer_case.supported_form_factors.all()]
        self.assertIn("ATX", supported)
        self.assertIn("Micro-ATX", supported)

    def test_string_representation(self):
        # Expected string uses the __str__ from the ComputerCase model.
        expected_str = (
            f"Manufacturer: {self.computer_case.manufacturer}\n"
            f"Name: {self.computer_case.name}\n"
            f"SKU: {self.computer_case.sku}\n"
            f"Price: ${self.computer_case.price:.2f}"
            f"\nForm Factor: {self.computer_case.form_factor},"
            f"\nColor: {self.computer_case.color},"
            f"\nSupported Form Factors: {self.computer_case.supported_form_factors}"
        )
        self.assertEqual(str(self.computer_case), expected_str)

    def test_check_compatibility_success(self):
        # Add a compatible motherboard with form factor 'ATX'
        self.parts_list.parts["Motherboard"] = [self.compatible_mb]
        issues = self.computer_case.check_compatibility(self.parts_list)
        self.assertEqual(issues, [])

    def test_check_compatibility_failure(self):
        # Add an incompatible motherboard (Mini-ITX) to the parts list.
        self.parts_list.parts["Motherboard"] = [self.incompatible_mb]
        issues = self.computer_case.check_compatibility(self.parts_list)
        # Expect at least one issue indicating incompatibility due to form factor.
        self.assertTrue(len(issues) > 0)
        self.assertTrue(any("not support" in issue.lower() or "incompatible" in issue.lower() for issue in issues))


if __name__ == '__main__':
    # Run tests with detailed output.
    unittest.main(verbosity=2)
