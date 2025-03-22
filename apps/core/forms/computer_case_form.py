from django import forms
from apps.core.models.cases import ComputerCase

class ListWidget(forms.TextInput):
    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        if value:
            return [x.strip() for x in value.strip("[]").split(",")]
        return []
    
class ComputerCaseForm(forms.ModelForm):
    class Meta:
        model = ComputerCase
        fields = ('manufacturer', 'name', 'sku', 'price', 'form_factor', 'color', 'supported_form_factors')
        
    supported_form_factors = forms.CharField(widget=ListWidget(attrs={'placeholder': "[ABC, XYZ]"}))