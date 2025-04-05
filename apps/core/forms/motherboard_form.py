from django import forms
from apps.core.models.motherboard import Motherboard

class MotherboardForm(forms.ModelForm):
    class Meta:
        model = Motherboard
        fields = ('manufacturer', 'name', 'sku', 'price', 'socket_type', 'form_factor', 'ram_slots',
                  'supported_ram_type', 'chipset_compatibility', 'bios_compatibility')