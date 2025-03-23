from django.shortcuts import redirect, render
from apps.core.forms.motherboard_form import MotherboardForm
from apps.core.models.motherboard import Motherboard

def motherboard_view(request):
    motherboard_form = MotherboardForm()

    if request.method == 'POST':
        if 'create_motherboard' in request.POST:
            motherboard_form = MotherboardForm(request.POST)
            if motherboard_form.is_valid():
                motherboard_form.save()
                return redirect('All Motherboards')

    all_motherboards = Motherboard.objects.all()

    return render(request, 'core/motherboard.html', {
        'motherboard_form': motherboard_form,
        'motherboards': all_motherboards,
    })