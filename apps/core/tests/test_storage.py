from django.test import TestCase
from apps.core.models.storage import Storage

class TestStorage(TestCase):
    def setUp(self):
        self.storage = Storage.objects.create(
            name="Samsung 970 EVO Plus",
            manufacturer="Samsung",
            price=129.99,
            sku=123450,

            storage_type="NVMe SSD",
            capacity_in_GB=1000,
            interface="PCIe 3.0 x4"
        )

    def test_initialization(self):
        self.assertEqual(self.storage.manufacturer, "Samsung")
        self.assertEqual(self.storage.name, "Samsung 970 EVO Plus")
        self.assertEqual(self.storage.sku, 123450)
        self.assertEqual(self.storage.price, 129.99)

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