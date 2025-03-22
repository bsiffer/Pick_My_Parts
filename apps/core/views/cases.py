from django.shortcuts import redirect, render
from apps.core.forms.computer_case_form import ComputerCaseForm
from apps.core.models.cases import ComputerCase

def cases(request):
    if request.method == 'POST':
        form = ComputerCaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('All Cases')
    else:
        form = ComputerCaseForm()

    all_cases = ComputerCase.objects.all()
    return render(request, 'core/cases.html', {'form': form, 'cases': all_cases})