from django.test import TestCase
from apps.core.models.cooling_accessory import CoolingAccessory

class TestCoolingAccessory(TestCase):
    def setUp(self):
        self.cooling_accessory = CoolingAccessory.objects.create(
            name="Noctua NH-D15",
            manufacturer="Noctua",
            price=89.99,
            sku=789456,
            cooling_type='Liquid'
        )

    def test_initialization(self):
        self.assertEqual(self.cooling_accessory.manufacturer, "Noctua")
        self.assertEqual(self.cooling_accessory.name, "Noctua NH-D15")
        self.assertEqual(self.cooling_accessory.sku, 789456)
        self.assertEqual(self.cooling_accessory.price, 89.99)
        self.assertEqual(self.cooling_accessory.cooling_type, 'Liquid')

    def test_string_representation(self):
        expected_str = (
            f"Manufacturer: {self.cooling_accessory.manufacturer}\n"
            f"Name: {self.cooling_accessory.name}\n"
            f"SKU: {self.cooling_accessory.sku}\n"
            f"Price: ${self.cooling_accessory.price:.2f}"
            f"\nCooling Type: {self.cooling_accessory.cooling_type}"
        )
        self.assertEqual(str(self.cooling_accessory), expected_str)