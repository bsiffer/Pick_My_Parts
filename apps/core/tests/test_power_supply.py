from django.test import TestCase
from apps.core.models.power_supply import PowerSupply

class TestGPU(TestCase):
    def setUp(self):
        self.power_supply = PowerSupply.objects.create(
            manufacturer="Corsair",
            name="Corsair RM850x",
            price=139.99,
            sku=8899550,

            size_standard="ATX",
            rated_wattage=850.00,
            certification_level="80 PLUS Gold",
            modular="Fully Modular",
            efficiency_rating_percentage=90.0,
            pcie_connectors=6,
            length_in_mm=160
        )

    def test_initialization(self):
        self.assertEqual(self.power_supply.manufacturer, "Corsair")
        self.assertEqual(self.power_supply.name, "Corsair RM850x")
        self.assertEqual(self.power_supply.sku, 8899550)
        self.assertEqual(self.power_supply.price, 139.99)

        self.assertEqual(self.power_supply.size_standard, "ATX")
        self.assertEqual(self.power_supply.rated_wattage, 850.0)
        self.assertEqual(self.power_supply.certification_level, "80 PLUS Gold")
        self.assertEqual(self.power_supply.modular, "Fully Modular")
        self.assertEqual(self.power_supply.efficiency_rating_percentage, 90.0)
        self.assertEqual(self.power_supply.pcie_connectors, 6)
        self.assertEqual(self.power_supply.length_in_mm, 160)

    def test_string_representation(self):
        expected_str = (
            f"Manufacturer: {self.power_supply.manufacturer}\n"
            f"Name: {self.power_supply.name}\n"
            f"SKU: {self.power_supply.sku}\n"
            f"Price: ${self.power_supply.price:.2f}\n"
            f"Size Standard: {self.power_supply.size_standard}\n"
            f"Wattage: {self.power_supply.rated_wattage}W\n"
            f"Certification: {self.power_supply.certification_level}\n"
            f"Modular: {self.power_supply.modular}\n"
            f"Efficiency Rating: {self.power_supply.efficiency_rating_percentage}%\n"
            f"PCIe Connectors: {self.power_supply.pcie_connectors}\n"
            f"Length: {self.power_supply.length_in_mm}mm"
        )
        self.assertEqual(str(self.power_supply), expected_str)