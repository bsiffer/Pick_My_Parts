from django.test import TestCase
from apps.core.models.ram import RAM

class TestRAM(TestCase):
    def setUp(self):
        self.ram =RAM.objects.create(
            manufacturer= 'Corsair',
            name='Vengeance',
            sku=173838,
            price=80.00,
            capacity_in_gb=16,
            ddr_standard="DDR4",
            speed_in_mhz=3200,
            stick=4,
            latency="CL16",
            rgb=False,
            color="Black"
        )
        
    def test_ram_creation(self):
        """Test if the RAM module is created with the correct attributes."""
        self.assertEqual(self.ram.manufacturer, "Corsair")
        self.assertEqual(self.ram.name, "Vengeance")
        self.assertEqual(self.ram.sku, 173838)
        self.assertEqual(self.ram.price, 80.00)
        self.assertEqual(self.ram.capacity_in_gb, 16)
        self.assertEqual(self.ram.ddr_standard, "DDR4")
        self.assertEqual(self.ram.speed_in_mhz, 3200)
        self.assertEqual(self.ram.sticks, 2)
        self.assertEqual(self.ram.latency, "CL16")
        self.assertTrue(self.ram.rgb)
        self.assertEqual(self.ram.color, "Black")

    def test_string_representation(self):
        expected_str = (
            f"{self.ram.manufacturer} - {self.ram.name} ({self.ram.sku})\n"
            f"Capacity: {self.ram.capacity_in_gb}GB\n"
            f"DDR Standard: {self.ram.ddr_standard}\n"
            f"Speed: {self.ram.speed_in_mhz}MHz\n"
            f"Sticks: {self.ram.sticks}\n"
            f"CAS Latency: {self.ram.latency}\n"
            f"RGB: Yes\n"
            f"Color: {self.ram.color}"
        )
        self.assertEqual(str(self.ram), expected_str)