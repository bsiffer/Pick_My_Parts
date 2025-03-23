from django import forms
from apps.core.models.power_supply import PowerSupply

class PowerSupplyForm(forms.ModelForm):
    class Meta:
        model = PowerSupply
        fields = ('manufacturer', 'name', 'sku', 'price', 'size_standard', 'rated_wattage', 'certification_level',
                  'modular', 'efficiency_rating_percentage', 'pcie_connectors', 'length_in_mm')