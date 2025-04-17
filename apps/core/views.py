from django.shortcuts import render

def gpu_view(request):
    return render(request, 'core/gpu.html')
