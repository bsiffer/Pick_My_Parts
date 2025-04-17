import unittest
from django.test import TestCase
from apps.core.models.part import Part
from apps.core.models.parts_list import PartsList


class MockPart(Part):
    """A mock Part for testing PartsList behavior."""
    def __init__(self, name, sku, part_type):
        # define internal variables (mock data)
        self._name = name
        self._sku = sku
        self._part_type = part_type
        self.manufacturer = "MockManufacturer"
        self.price = 0.0

    def get_name(self):
        return self._name

    def get_sku(self):
        return self._sku

    def set_name(self, new_name):
        self._name = new_name

    def display_info(self):
        return f"Part Name: {self._name}, SKU: {self._sku}"

    def check_compatibility(self, parts_list):
        # For mock testing, simply return an empty list indicating no issues.
        return []

    def get_part_type(self):
        return self._part_type

class TestPartsList(TestCase):
    def setUp(self):
        self.parts_list = PartsList()
        self.cpu = MockPart("CPU Mock", 1001, "CPU")
        self.ram = MockPart("RAM Mock", 1002, "RAM")
        self.gpu = MockPart("GPU Mock", 1003, "GPU")

    def test_add_part(self):
        self.parts_list.add_part(self.cpu)
        self.assertIn(self.cpu, self.parts_list.parts["CPU"])

    def test_add_duplicate_part(self):
        self.parts_list.add_part(self.cpu)
        self.parts_list.add_part(self.cpu)
        self.assertEqual(len(self.parts_list.parts["CPU"]), 2)

    def test_remove_part(self):
        self.parts_list.add_part(self.cpu)
        self.parts_list.remove_part(1001)
        self.assertNotIn(self.cpu, self.parts_list.parts["CPU"])

    def test_remove_one_of_multiple_parts(self):
        self.parts_list.add_part(self.cpu)
        self.parts_list.add_part(self.cpu)
        self.parts_list.remove_part(1001)
        self.assertEqual(len(self.parts_list.parts["CPU"]), 1)

    def test_update_part(self):
        self.parts_list.add_part(self.cpu)
        self.parts_list.update_part(1001, "_name", "Updated CPU")
        self.assertEqual(self.parts_list.parts["CPU"][0].get_name(), "Updated CPU")

    def test_clear_list(self):
        # Add parts to multiple categories.
        self.parts_list.add_part(self.cpu)
        self.parts_list.add_part(self.ram)
        self.parts_list.add_part(self.gpu)
        self.parts_list.clear_list()
        # All lists in the dictionary should now be empty.
        for key in self.parts_list.parts:
            self.assertEqual(self.parts_list.parts[key], [])

    def test_check_compatibility(self):
        # Add our mock parts.
        self.parts_list.add_part(self.cpu)
        self.parts_list.add_part(self.ram)
        self.parts_list.add_part(self.gpu)
        # Check compatibility for CPU parts.
        result = self.parts_list.check_compatibility("CPU")
        # Our mock returns no issues.
        self.assertEqual(result["incompatibilities"], [])
        # Verify that the compatible parts list contains the CPU.
        self.assertIn(self.cpu, result["compatible_parts"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
