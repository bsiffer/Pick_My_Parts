from django.shortcuts import redirect, render
from apps.core.forms.power_supply_form import PowerSupplyForm
from apps.core.models.power_supply import PowerSupply

def power_supply_view(request):
    power_supply_form = PowerSupplyForm()

    if request.method == 'POST':
        if 'create_power_supply' in request.POST:
            power_supply_form = PowerSupplyForm(request.POST)
            if power_supply_form.is_valid():
                power_supply_form.save()
                return redirect('All Power Supplies')

    all_power_supplies = PowerSupply.objects.all()

    return render(request, 'core/power_supply.html', {
        'power_supply_form': power_supply_form,
        'power_supplies': all_power_supplies,
    })