from django.test import TestCase
from apps.core.models.computer_case import ComputerCase
from apps.core.models.form_factor import FormFactor

class TestComputerCase(TestCase):
    def setUp(self):
        atx_form_factor = FormFactor.objects.get_or_create(name="ATX")[0]
        micro_atx_form_factor = FormFactor.objects.get_or_create(name="Micro-ATX")[0]
        mini_itx_form_factor = FormFactor.objects.get_or_create(name="Mini-ITX")[0]

        self.case = ComputerCase.objects.create(
            manufacturer="NZXT",
            name="H510",
            sku=123456,
            price=99.99,
            form_factor=atx_form_factor,
            color="Black"
        )

        self.case.supported_form_factors.set([atx_form_factor, micro_atx_form_factor, mini_itx_form_factor])
    
    def test_initialization(self):
        self.assertEqual(self.case.manufacturer, "NZXT")
        self.assertEqual(self.case.name, "H510")
        self.assertEqual(self.case.sku, 123456)
        self.assertEqual(self.case.price, 99.99)
        self.assertEqual(self.case.form_factor.name, "ATX")
        self.assertEqual(self.case.color, "Black")
        self.assertListEqual(
            [form_factor.name for form_factor in self.case.supported_form_factors.all()],
            ["ATX", "Micro-ATX", "Mini-ITX"]
        )
