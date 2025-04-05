from django import forms
from apps.core.models.cpu import CPU

class CPUForm(forms.ModelForm):
    class Meta:
        model = CPU
        fields = ('manufacturer', 'name', 'sku', 'price', 'architecture', 'clock_speed', 'ddr4_compatibility',
                  'ddr5_compatibility', 'socket_type', 'wattage_compatibility',
                  'bios_compatibility', 'chipset_compatibility')