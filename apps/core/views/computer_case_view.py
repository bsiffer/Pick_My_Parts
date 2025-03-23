from django.shortcuts import redirect, render
from apps.core.forms.computer_case_form import ComputerCaseForm
from apps.core.forms.form_factor_form import FormFactorForm
from apps.core.models.computer_case import ComputerCase
from apps.core.models.form_factor import FormFactor

def computer_case_view(request):
    computer_case_form = ComputerCaseForm()
    form_factor_form = FormFactorForm()

    if request.method == 'POST':
        if 'create_computer_case' in request.POST:
            computer_case_form = ComputerCaseForm(request.POST)
            if computer_case_form.is_valid():
                computer_case_form.save()
                return redirect('All Computer Cases')
        elif 'create_form_factor' in request.POST:
            form_factor_form = FormFactorForm(request.POST)
            if form_factor_form.is_valid():
                form_factor_form.save()
                return redirect('All Computer Cases')
    
    all_cases = ComputerCase.objects.all()
    all_form_factors = FormFactor.objects.all()

    return render(request, 'core/computer_case.html', {
        'computer_case_form': computer_case_form,
        'form_factor_form': form_factor_form,
        'computer_cases': all_cases,
        'form_factors': all_form_factors
    })