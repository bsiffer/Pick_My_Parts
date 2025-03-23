from django.shortcuts import redirect, render
from apps.core.forms.cooling_accessory_form import CoolingAccessoryForm
from apps.core.models.cooling_accessory import CoolingAccessory

def cooling_accessory_view(request):
    cooling_accessory_form = CoolingAccessoryForm()

    if request.method == 'POST':
        if 'create_cooling_accessory' in request.POST:
            cooling_accessory_form = CoolingAccessoryForm(request.POST)
            if cooling_accessory_form.is_valid():
                cooling_accessory_form.save()
                return redirect('All Cooling Accessories')

    all_cooling_accessories = CoolingAccessory.objects.all()

    return render(request, 'core/cooling_accessory.html', {
        'cooling_accessory_form': cooling_accessory_form,
        'cooling_accessories': all_cooling_accessories,
    })