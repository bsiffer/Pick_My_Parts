from django.shortcuts import redirect, render
from apps.core.forms.gpu_form import GPUForm
from apps.core.models.gpu import GPU

def gpu_view(request):
    gpu_form = GPUForm()

    if request.method == 'POST':
        if 'create_gpu' in request.POST:
            gpu_form = GPUForm(request.POST)
            if gpu_form.is_valid():
                gpu_form.save()
                return redirect('All GPUs')

    all_gpus = GPU.objects.all()

    return render(request, 'core/gpu.html', {
        'gpu_form': gpu_form,
        'gpus': all_gpus,
    })