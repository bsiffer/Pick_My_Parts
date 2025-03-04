import unittest
from apps.core.models.cases import ComputerCase
from apps.core.models.motherboard import Motherboard

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
        manufacturer = "ASUS"
        name = "ROG STRIX B550-F Gaming"
        sku = 1234567
        price = 189.99
        architecture = "x86-64"
        standard_size = "ATX"
        ram_slots = 4
        compatibility = ["AMD Ryzen 3000 Series", "AMD Ryzen 5000 Series"]

        self.assertTrue(self.case.is_compatible(Motherboard(manufacturer, name, sku, price,
                                                            architecture, standard_size, ram_slots, compatibility)))

        standard_size = "Micro-ATX"
        self.assertTrue(self.case.is_compatible(Motherboard(manufacturer, name, sku, price,
                                                            architecture, standard_size, ram_slots, compatibility)))

        standard_size = "E-ATX"
        self.assertFalse(self.case.is_compatible(Motherboard(manufacturer, name, sku, price,
                                                             architecture, standard_size, ram_slots, compatibility)))
    
    def test_to_string(self):
        expected_output = ("Part Name: H510\nPrice: 99.99\nSKU: 123456\nManufacturer: NZXT\n"
                           "Size: ATX, Color: Black, Compatible with: ATX, Micro-ATX, Mini-ITX")
        self.assertEqual(self.case.to_string(), expected_output)

if __name__ == "__main__":
    unittest.main()
