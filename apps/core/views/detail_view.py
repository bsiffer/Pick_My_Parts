from django.shortcuts import  render
from apps.core.models.computer_case import ComputerCase
from apps.core.models.cooling_accessory import CoolingAccessory
from apps.core.models.cpu import CPU
from apps.core.models.gpu import GPU
from apps.core.models.motherboard import Motherboard
from apps.core.models.power_supply import PowerSupply
from apps.core.models.ram import RAM
from apps.core.models.storage import Storage

model_map = {
    'CPU': CPU,
    'Motherboard': Motherboard,
    'GPU': GPU,
    'RAM': RAM,
    'PowerSupply': PowerSupply,
    'ComputerCase': ComputerCase,
    'Storage': Storage,
    'CoolingAccessory': CoolingAccessory,
}

def detail_view(request, model_name, sku):
    model = model_map.get(model_name)

    if model:
        part = model.objects.filter(sku=sku).first()

        return render(request, f'core/detail/{model_name}_detail.html', {
            'part': part,
        })
    else:
        return render(request, 'core/not_found.html', {})   