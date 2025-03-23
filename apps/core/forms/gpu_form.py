from django import forms
from apps.core.models.gpu import GPU

class GPUForm(forms.ModelForm):
    class Meta:
        model = GPU
        fields = ('manufacturer', 'name', 'sku', 'price', 'architecture', 'memory_bus', 'pcie_standard', 'slot_size',
                  'length', 'cooling_type', 'power_requirement', 'power_connectors', 'color')