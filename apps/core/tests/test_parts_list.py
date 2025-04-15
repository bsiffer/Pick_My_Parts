import unittest
from apps.core.models.part import Part
from apps.core.models.parts_list import PartsList


class MockPart(Part):
    """Mock part class for testing purposes."""

    def __init__(self, name, sku, part_type):
        self._name = name
        self._sku = sku
        self._part_type = part_type

    def get_name(self):
        return self._name

    def get_sku(self):
        return self._sku

    def set_name(self, new_name):
        self._name = new_name

    def display_info(self):
        return f"Part Name: {self._name}, SKU: {self._sku}"

    def check_compatibility(self, parts_list):
        return []  # No compatibility issues for test cases

    def get_part_type(self):
        return self._part_type


class TestPartsList(unittest.TestCase):
    def setUp(self):
        self.parts_list = PartsList()
        self.part1 = MockPart("CPU", 1001, "CPU")
        self.part2 = MockPart("RAM", 1002, "RAM")
        self.part3 = MockPart("GPU", 1003, "GPU")

    def test_add_part(self):
        print("Testing adding a single part to the list...")
        self.parts_list.add_part(self.part1)
        self.assertIn(self.part1, self.parts_list.parts["CPU"])

    def test_add_duplicate_part(self):
        print("Testing adding multiple parts with the same SKU...")
        self.parts_list.add_part(self.part1)
        self.parts_list.add_part(self.part1)
        self.assertEqual(len(self.parts_list.parts["CPU"]), 2)

    def test_remove_part(self):
        print("Testing removing a part by SKU...")
        self.parts_list.add_part(self.part1)
        self.parts_list.remove_part(1001)
        self.assertNotIn(self.part1, self.parts_list.parts["CPU"])

    def test_remove_one_of_multiple_parts(self):
        print("Testing removing one instance of a part when multiple exist...")
        self.parts_list.add_part(self.part1)
        self.parts_list.add_part(self.part1)
        self.parts_list.remove_part(1001)
        self.assertEqual(len(self.parts_list.parts["CPU"]), 1)

    def test_update_part(self):
        print("Testing updating an attribute of a part...")
        self.parts_list.add_part(self.part1)
        self.parts_list.update_part(1001, "_name", "Updated CPU")
        self.assertEqual(self.parts_list.parts["CPU"][0].get_name(), "Updated CPU")

    def test_get_part(self):
        print("Testing retrieving a part by SKU...")
        self.parts_list.add_part(self.part1)

        part_found = None
        for part in self.parts_list.parts["CPU"]:
            if part.get_sku() == 1001:
                part_found = part
                break

        self.assertIsNotNone(part_found)
        self.assertEqual(part_found.get_name(), "CPU")
        self.assertEqual(part_found.get_sku(), 1001)

    def test_clear_list(self):
        print("Testing clearing the parts list...")
        self.parts_list.add_part(self.part1)
        self.parts_list.clear_list()
        self.assertEqual(len(self.parts_list.parts["CPU"]), 0)

    def test_check_compatibility(self):
        print("Testing compatibility check function...")
        self.parts_list.add_part(self.part1)
        self.parts_list.check_compatibility('CPU')
        self.assertEqual(len(self.parts_list.incompatibilities), 0)


if __name__ == "__main__":
    unittest.main()
