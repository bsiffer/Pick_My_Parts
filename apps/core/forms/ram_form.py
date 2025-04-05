from django import forms
from apps.core.models.ram import RAM

class RAMForm(forms.ModelForm):
    class Meta:
        model = RAM
        fields = ('manufacturer', 'name', 'sku', 'price', 'capacity_in_gb', 'ddr_standard', 'speed_in_mhz', 'sticks', 'latency', 'rgb', 'color')