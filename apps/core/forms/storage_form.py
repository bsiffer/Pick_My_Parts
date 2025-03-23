from django import forms
from apps.core.models.storage import Storage

class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ('manufacturer', 'name', 'sku', 'price', 'storage_type', 'capacity_in_GB', 'interface')