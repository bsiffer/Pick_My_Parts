import unittest
from src.models.part import Part
from src.models.parts_list import PartsList

class MockPart(Part):
    """Mock part class for testing purposes."""
    def __init__(self, name, sku):
        self._name = name
        self._sku = sku
    
    def get_name(self):
        return self._name
    
    def get_sku(self):
        return self._sku
    
    def display_info(self):
        return f"Part Name: {self._name}, SKU: {self._sku}"
    
    def check_compatibility(self, parts_list):
        return []  # No compatibility issues for test cases

class TestPartsList(unittest.TestCase):
    def setUp(self):
        self.parts_list = PartsList()
        self.part1 = MockPart("CPU", 1001)
        self.part2 = MockPart("RAM", 1002)
        self.part3 = MockPart("GPU", 1003)

    def test_add_part(self):
        print("Testing adding a single part to the list...")
        self.parts_list.add_part(self.part1)
        self.assertIn(1001, self.parts_list.parts)
        self.assertEqual(len(self.parts_list.parts[1001]), 1)
    
    def test_add_duplicate_part(self):
        print("Testing adding multiple parts with the same SKU...")
        self.parts_list.add_part(self.part1)
        self.parts_list.add_part(self.part1)
        self.assertEqual(len(self.parts_list.parts[1001]), 2)
    
    def test_remove_part(self):
        print("Testing removing a part by SKU...")
        self.parts_list.add_part(self.part1)
        self.parts_list.remove_part(1001)
        self.assertNotIn(1001, self.parts_list.parts)
    
    def test_remove_one_of_multiple_parts(self):
        print("Testing removing one instance of a part when multiple exist...")
        self.parts_list.add_part(self.part1)
        self.parts_list.add_part(self.part1)
        self.parts_list.remove_part(1001)
        self.assertEqual(len(self.parts_list.parts[1001]), 1)
    
    def test_update_part(self):
        print("Testing updating an attribute of a part...")
        self.parts_list.add_part(self.part1)
        self.parts_list.update_part(1001, "_name", "Updated CPU")
        self.assertEqual(self.parts_list.parts[1001][0].get_name(), "Updated CPU")
    
    def test_get_part(self):
        print("Testing retrieving a part by SKU...")
        self.parts_list.add_part(self.part1)
        self.assertEqual(self.parts_list.get_part(1001)[0].get_name(), "CPU")
    
    def test_clear_list(self):
        print("Testing clearing the parts list...")
        self.parts_list.add_part(self.part1)
        self.parts_list.clear_list()
        self.assertEqual(len(self.parts_list.parts), 0)
    
    def test_check_compatibility(self):
        print("Testing compatibility check function...")
        self.parts_list.add_part(self.part1)
        self.parts_list.check_compatibility()
        self.assertEqual(len(self.parts_list.incompatibilities), 0)
    
if __name__ == "__main__":
    unittest.main()
    