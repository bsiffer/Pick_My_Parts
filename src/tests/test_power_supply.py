import unittest
from src.models.power_supply import PowerSupply


class TestPowerSupply(unittest.TestCase):
    def setUp(self):
        """create a sample power supply object for testing"""
        self.sample_psu = PowerSupply(
            manufacturer="SilverStone",
            name="SX750",
            sku=67890,
            price=139.99,
            size_standard="SFX",
            rated_wattage=750,
            certification_level="80+ Platinum",
            modular="Fully Modular",
            efficiency_rating_percentage=92.0,
            pcie_connectors=6,
            length=125
        )

    # test getter methods
    def test_get_size_standard(self):
        self.assertEqual(self.sample_psu.get_size_standard(), "SFX")

    def test_get_rated_wattage(self):
        self.assertEqual(self.sample_psu.get_rated_wattage(), 750)

    def test_get_certification_level(self):
        self.assertEqual(self.sample_psu.get_certification_level(), "80+ Platinum")

    def test_get_modular(self):
        self.assertEqual(self.sample_psu.get_modular(), "Fully Modular")

    def test_get_efficiency_rating_percentage(self):
        self.assertEqual(self.sample_psu.get_efficiency_rating_percentage(), 92.0)

    def test_get_pcie_connectors(self):
        self.assertEqual(self.sample_psu.get_pcie_connectors(), 6)

    def test_get_length(self):
        self.assertEqual(self.sample_psu.get_length(), 125)

    # test setter methods
    def test_set_size_standard(self):
        self.sample_psu.set_size_standard("ATX")
        self.assertEqual(self.sample_psu.get_size_standard(), "ATX")

    def test_set_rated_wattage(self):
        self.sample_psu.set_rated_wattage(850)
        self.assertEqual(self.sample_psu.get_rated_wattage(), 850)

    def test_set_certification_level(self):
        self.sample_psu.set_certification_level("80+ Gold")
        self.assertEqual(self.sample_psu.get_certification_level(), "80+ Gold")

    def test_set_modular(self):
        self.sample_psu.set_modular("Semi-Modular")
        self.assertEqual(self.sample_psu.get_modular(), "Semi-Modular")

    def test_set_efficiency_rating_percentage(self):
        self.sample_psu.set_efficiency_rating_percentage(90.5)
        self.assertEqual(self.sample_psu.get_efficiency_rating_percentage(), 90.5)

    def test_set_pcie_connectors(self):
        self.sample_psu.set_pcie_connectors(4)
        self.assertEqual(self.sample_psu.get_pcie_connectors(), 4)

    def test_set_length(self):
        self.sample_psu.set_length(130)
        self.assertEqual(self.sample_psu.get_length(), 130)

    # test to_string method
    def test_to_string(self):
        expected_output = (f"Part Name: SX750\nPrice: 139.99\n"
                           f"SKU: 67890\nManufacturer: SilverStone\n"
            "size standard: SFX\n"
            "wattage: 750W\n"
            "certification: 80+ Platinum\n"
            "modular: Fully Modular\n"
            "efficiency rating: 92.0%\n"
            "pcie connectors: 6\n"
            "length: 125mm"
        )
        self.assertEqual(self.sample_psu.to_string(), expected_output)
