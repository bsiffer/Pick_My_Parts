from django.test import TestCase
from apps.core.models.form_factor import FormFactor

class TestFormFactor(TestCase):
    def setUp(self):
        self.form_factor = FormFactor.objects.create(
            name="ATX"
        )

    def test_initialization(self):
        self.assertEqual(self.form_factor.name, "ATX")

    def test_string_representation(self):
        expected_str = (
            f"{self.form_factor.name}"
        )
        self.assertEqual(str(self.form_factor), expected_str)