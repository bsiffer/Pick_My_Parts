from django.shortcuts import render

def cpus(request):
    return render(request, 'core/cpus.html', {})