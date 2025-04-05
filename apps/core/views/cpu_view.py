from django.shortcuts import redirect, render
from apps.core.forms.cpu_form import CPUForm
from apps.core.models.cpu import CPU

def cpu_view(request):
    cpu_form = CPUForm()

    if request.method == 'POST':
        if 'create_cpu' in request.POST:
            cpu_form = CPUForm(request.POST)
            if cpu_form.is_valid():
                cpu_form.save()
                return redirect('All CPUs')

    all_cpus = CPU.objects.all()

    return render(request, 'core/cpu.html', {
        'cpu_form': cpu_form,
        'cpus': all_cpus,
    })