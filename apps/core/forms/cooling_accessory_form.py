from django import forms
from apps.core.models.cooling_accessory import CoolingAccessory

class CoolingAccessoryForm(forms.ModelForm):
    class Meta:
        model = CoolingAccessory
        fields = ('manufacturer', 'name', 'sku', 'price', 'cooling_type')