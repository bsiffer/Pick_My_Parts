import unittest
from django.test import TestCase
from apps.core.models.form_factor import FormFactor


class TestFormFactor(TestCase):
    def setUp(self):
        self.form_factor = FormFactor.objects.create(name="ATX")

    def test_initialization(self):
        # Verify that the form factor is properly set
        self.assertEqual(self.form_factor.name, "ATX")

    def test_string_representation(self):
        # The __str__ method should return the name
        expected_str = "ATX"
        self.assertEqual(str(self.form_factor), expected_str)


if __name__ == '__main__':
    # Set verbosity=2 for detailed output when running this test file directly.
    unittest.main(verbosity=2)
