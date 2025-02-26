import unittest
from src.models.cases import ComputerCase

class TestComputerCase(unittest.TestCase):
    def setUp(self):
        self.case = ComputerCase("NZXT", "H510", 123456, 99.99, "ATX", "Black", ["ATX", "Micro-ATX", "Mini-ITX"])
    
    def test_initialization(self):
        self.assertEqual(self.case.get_manufacturer(), "NZXT")
        self.assertEqual(self.case.get_name(), "H510")
        self.assertEqual(self.case.get_sku(), 123456)
        self.assertEqual(self.case.get_price(), 99.99)
        self.assertEqual(self.case.size, "ATX")
        self.assertEqual(self.case.color, "Black")
        self.assertListEqual(self.case.compatibility, ["ATX", "Micro-ATX", "Mini-ITX"])
    
    def test_is_compatible(self):
        self.assertTrue(self.case.is_compatible("ATX"))
        self.assertTrue(self.case.is_compatible("Micro-ATX"))
        self.assertFalse(self.case.is_compatible("E-ATX"))
    
    def test_to_string(self):
        expected_output = ("Part Name: H510\nPrice: 99.99\nSKU: 123456\nManufacturer: NZXT\n"
                           "Size: ATX, Color: Black, Compatible with: ATX, Micro-ATX, Mini-ITX")
        self.assertEqual(self.case.to_string(), expected_output)

if __name__ == "__main__":
    unittest.main()
