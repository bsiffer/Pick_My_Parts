from django.shortcuts import render
from apps.core.forms.build_form import BuildForm

def build(request):
    form = BuildForm()
    return render(request, 'core/build.html', {'form': form})