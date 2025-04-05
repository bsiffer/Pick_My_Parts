from django import forms
from apps.core.models.computer_case import ComputerCase
from apps.core.models.cooling_accessory import CoolingAccessory
from apps.core.models.cpu import CPU
from apps.core.models.gpu import GPU
from apps.core.models.motherboard import Motherboard
from apps.core.models.ram import RAM
from apps.core.models.storage import Storage

class BuildForm(forms.Form):
    cpu = forms.ModelChoiceField(
        queryset=CPU.objects.all(),
        widget=forms.TextInput(attrs={'list': 'cpu_suggestions'}),
        required=False
    )
    motherboard = forms.ModelChoiceField(
        queryset=Motherboard.objects.all(),
        widget=forms.TextInput(attrs={'list': 'motherboard_suggestions'}),
        required=False
    )
    gpu = forms.ModelChoiceField(
        queryset=GPU.objects.all(),
        widget=forms.TextInput(attrs={'list': 'gpu_suggestions'}),
        required=False
    )
    ram = forms.ModelChoiceField(
        queryset=RAM.objects.all(),
        widget=forms.TextInput(attrs={'list': 'ram_suggestions'}),
        required=False
    )
    storage = forms.ModelChoiceField(
        queryset=Storage.objects.all(),
        widget=forms.TextInput(attrs={'list': 'storage_suggestions'}),
        required=False
    )
    computer_case = forms.ModelChoiceField(
        queryset=ComputerCase.objects.all(),
        widget=forms.TextInput(attrs={'list': 'case_suggestions'}),
        required=False
    )
    cooling_accessory = forms.ModelChoiceField(
        queryset=CoolingAccessory.objects.all(),
        widget=forms.TextInput(attrs={'list': 'cooling_accessory_suggestions'}),
        required=False
    )