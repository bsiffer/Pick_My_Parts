from django.test import TestCase
from apps.core.models.gpu import GPU

class TestGPU(TestCase):
    def setUp(self):
        self.gpu = GPU.objects.create(
            name="NVIDIA GeForce RTX 4090",
            manufacturer="NVIDIA",
            price=1599.99,
            sku=889955,

            architecture="Ada Lovelace",
            memory_bus=384,
            pcie_standard="PCIe 4.0",
            slot_size="Triple Slot",
            length_in_mm=304.0,
            cooling_type="Air Cooler",
            power_requirement=450.0,
            power_connectors="3x 8-pin",
            color="Black"
        )

    def test_initialization(self):
        self.assertEqual(self.gpu.manufacturer, "NVIDIA")
        self.assertEqual(self.gpu.name, "NVIDIA GeForce RTX 4090")
        self.assertEqual(self.gpu.sku, 889955)
        self.assertEqual(self.gpu.price, 1599.99)

        self.assertEqual(self.gpu.architecture, "Ada Lovelace")
        self.assertEqual(self.gpu.memory_bus, 384)
        self.assertEqual(self.gpu.pcie_standard, "PCIe 4.0")
        self.assertEqual(self.gpu.slot_size, "Triple Slot")
        self.assertEqual(self.gpu.length_in_mm, 304.0)
        self.assertEqual(self.gpu.cooling_type, "Air Cooler")
        self.assertEqual(self.gpu.power_requirement, 450.0)
        self.assertEqual(self.gpu.power_connectors, "3x 8-pin")
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