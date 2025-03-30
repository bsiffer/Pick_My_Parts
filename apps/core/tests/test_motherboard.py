from django.test import TestCase
from apps.core.models.motherboard import Motherboard

class TestMotherboard(TestCase):
    def setUp(self):
        """Set up a sample motherboard for testing."""
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
        )

    def test_motherboard_creation(self):
        """Test if the motherboard is created with correct attributes."""
        self.assertEqual(self.motherboard.manufacturer, "ASUS")
        self.assertEqual(self.motherboard.name, "ROG Strix B550-F")
        self.assertEqual(self.motherboard.sku, 654321)
        self.assertEqual(self.motherboard.price, 179.99)
        self.assertEqual(self.motherboard.socket_type, "AM4")
        self.assertEqual(self.motherboard.form_factor, "ATX")
        self.assertEqual(self.motherboard.ram_slots, 4)
        self.assertEqual(self.motherboard.supported_ram_type, "DDR4")
        self.assertEqual(self.motherboard.chipset_compatibility, "B550")
        self.assertEqual(self.motherboard.bios_compatibility, "UEFI")

    def test_string_representation(self):
        """Test the string rep of the motherboard."""
        expected_str = (
            f"Manufacturer: {self.motherboard.manufacturer}\n"
            f"Name: {self.motherboard.name}\n"
            f"SKU: {self.motherboard.sku}\n"
            f"Price: ${self.motherboard.price:.2f}"
            f"\nSocket Type: {self.motherboard.socket_type}, Form Factor: {self.motherboard.form_factor}, "
            f"RAM Slots: {self.motherboard.ram_slots}, Supported RAM Type: {self.motherboard.supported_ram_type}"
        )
        self.assertEqual(str(self.motherboard), expected_str)
