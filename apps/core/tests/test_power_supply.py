import unittest
from django.test import TestCase
from apps.core.models.power_supply import PowerSupply


class TestPowerSupply(TestCase):
    def setUp(self):
        self.psu = PowerSupply.objects.create(
            manufacturer="Corsair",
            name="Corsair RM850x",
            sku=8899550,
            price=139.99,
            size_standard="ATX",
            rated_wattage=850.00,
            certification_level="80 PLUS Gold",
            modular="Fully Modular",
            efficiency_rating_percentage=90.0,
            pcie_connectors=6,
            length_in_mm=160
        )

    def test_initialization(self):
        self.assertEqual(self.psu.manufacturer, "Corsair")
        self.assertEqual(self.psu.name, "Corsair RM850x")
        self.assertEqual(self.psu.sku, 8899550)
        self.assertAlmostEqual(float(self.psu.price), 139.99)
        self.assertEqual(self.psu.size_standard, "ATX")
        self.assertAlmostEqual(float(self.psu.rated_wattage), 850.00)
        self.assertEqual(self.psu.certification_level, "80 PLUS Gold")
        self.assertEqual(self.psu.modular, "Fully Modular")
        self.assertAlmostEqual(float(self.psu.efficiency_rating_percentage), 90.0)
        self.assertEqual(self.psu.pcie_connectors, 6)
        self.assertEqual(self.psu.length_in_mm, 160)

    def test_string_representation(self):
        expected_str = (
            f"Manufacturer: {self.psu.manufacturer}\n"
            f"Name: {self.psu.name}\n"
            f"SKU: {self.psu.sku}\n"
            f"Price: ${self.psu.price:.2f}\n"
            f"Size Standard: {self.psu.size_standard}\n"
            f"Wattage: {self.psu.rated_wattage}W\n"
            f"Certification: {self.psu.certification_level}\n"
            f"Modular: {self.psu.modular}\n"
            f"Efficiency Rating: {self.psu.efficiency_rating_percentage}%\n"
            f"PCIe Connectors: {self.psu.pcie_connectors}\n"
            f"Length: {self.psu.length_in_mm}mm"
        )
        self.assertEqual(str(self.psu), expected_str)


if __name__ == '__main__':
    # Using verbosity=2 to display detailed test output when running the file directly.
    unittest.main(verbosity=2)
