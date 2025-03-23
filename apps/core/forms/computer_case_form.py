from django import forms
from apps.core.models.cases import ComputerCase
from apps.core.models.form_factor import FormFactor


class ComputerCaseForm(forms.ModelForm):
    supported_form_factors = forms.ModelMultipleChoiceField(
        queryset=FormFactor.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = ComputerCase
        fields = ('manufacturer', 'name', 'sku', 'price', 'form_factor', 'color', 'supported_form_factors')