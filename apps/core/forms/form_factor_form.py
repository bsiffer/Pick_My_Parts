from django import forms
from apps.core.models.form_factor import FormFactor

class FormFactorForm(forms.ModelForm):
    class Meta:
        model = FormFactor
        fields = ('name',)