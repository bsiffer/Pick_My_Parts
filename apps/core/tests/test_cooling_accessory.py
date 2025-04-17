import unittest
from django.test import TestCase
from apps.core.models.cooling_accessory import CoolingAccessory
from apps.core.models.cpu import CPU
from apps.core.models.computer_case import ComputerCase
from apps.core.models.form_factor import FormFactor
from apps.core.models.parts_list import PartsList


class TestCoolingAccessory(TestCase):
    def setUp(self):
        # create a CoolingAccessory instance with supported sockets
        self.cooling_accessory = CoolingAccessory.objects.get_or_create(
            manufacturer="Noctua",
            name="NH-D15",
            sku=800001,
            price=89.99,
            cooling_type="Air Cooler",
            supported_sockets=["LGA1700", "LGA1151"]
        )[0]

        # create a CPU instance with a socket type that is supported
        self.cpu = CPU.objects.get_or_create(
            manufacturer="Intel",
            name="Core i9-13900K",
            sku=100010,
            price=589.99,
            architecture="Raptor Lake",
            clock_speed=5.8,
            ddr4_compatibility=True,
            ddr5_compatibility=True,
            socket_type="LGA1700",
            wattage_compatibility=125.0,
            bios_compatibility="UEFI",
            chipset_compatibility="Z690"
        )[0]

        # create a FormFactor instance for the case
        self.ff_atx, _ = FormFactor.objects.get_or_create(name="ATX")

        # create a ComputerCase instance that supports Air Cooler
        self.computer_case = ComputerCase.objects.get_or_create(
            manufacturer="NZXT",
            name="H510",
            sku=700001,
            price=69.99,
            form_factor=self.ff_atx,
            color="Black"
        )[0]
        # Set supported cooling types and supported form factors
        self.computer_case.supported_cooling_types = ["Air Cooler", "Liquid Cooler"]
        self.computer_case.save()
        self.computer_case.supported_form_factors.set([self.ff_atx])

        # create a PartsList instance and add the CPU and ComputerCase
        self.parts_list = PartsList()
        self.parts_list.parts["CPU"] = [self.cpu]
        self.parts_list.parts["ComputerCase"] = [self.computer_case]

    def test_initialization(self):
        # verify all attributes of the CoolingAccessory
        self.assertEqual(self.cooling_accessory.manufacturer, "Noctua")
        self.assertEqual(self.cooling_accessory.name, "NH-D15")
        self.assertEqual(self.cooling_accessory.sku, 800001)
        self.assertAlmostEqual(float(self.cooling_accessory.price), 89.99)
        self.assertEqual(self.cooling_accessory.cooling_type, "Air Cooler")
        self.assertEqual(self.cooling_accessory.supported_sockets, ["LGA1700", "LGA1151"])

    def test_string_representation(self):
        expected_str = (
            f"Manufacturer: {self.cooling_accessory.manufacturer}\n"
            f"Name: {self.cooling_accessory.name}\n"
            f"SKU: {self.cooling_accessory.sku}\n"
            f"Price: ${self.cooling_accessory.price:.2f}\n"
            f"Cooling Type: {self.cooling_accessory.cooling_type}"
        )
        self.assertEqual(str(self.cooling_accessory), expected_str)

    def test_check_compatibility_success(self):
        # should return no issues
        issues = self.cooling_accessory.check_compatibility(self.parts_list)
        self.assertEqual(issues, [])

    def test_check_compatibility_failure_due_to_socket(self):
        # change the CPU's socket type to one not supported by the cooling accessory
        self.cpu.socket_type = "AM4"
        self.cpu.save()
        issues = self.cooling_accessory.check_compatibility(self.parts_list)
        self.assertTrue(any("incompatible" in issue.lower() for issue in issues))

    def test_check_compatibility_failure_due_to_case(self):
        # change to exclude Air Cooler
        self.computer_case.supported_cooling_types = ["Liquid Cooler"]
        self.computer_case.save()
        issues = self.cooling_accessory.check_compatibility(self.parts_list)
        self.assertTrue(any("incompatible" in issue.lower() for issue in issues))


if __name__ == '__main__':
    unittest.main(verbosity=2)
