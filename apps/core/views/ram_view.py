from django.shortcuts import redirect, render
from apps.core.forms.ram_form import RAMForm
from apps.core.models.ram import RAM

def ram_view(request):
    ram_form = RAMForm()

    if request.method == 'POST':
        if 'create_ram' in request.POST:
            ram_form = RAMForm(request.POST)
            if ram_form.is_valid():
                ram_form.save()
                return redirect('All RAMs')

    all_rams = RAM.objects.all()

    return render(request, 'core/ram.html', {
        'ram_form': ram_form,
        'rams': all_rams,
    })