from django.contrib import admin
from apps.core.models.computer_case import ComputerCase
from apps.core.models.cooling_accessory import CoolingAccessory
from apps.core.models.cpu import CPU
from apps.core.models.form_factor import FormFactor
from apps.core.models.gpu import GPU
from apps.core.models.motherboard import Motherboard
from apps.core.models.power_supply import PowerSupply
from apps.core.models.ram import RAM
from apps.core.models.storage import Storage

# Register your models here.
admin.site.register(FormFactor)
admin.site.register(ComputerCase)
admin.site.register(CoolingAccessory)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(Motherboard)
admin.site.register(PowerSupply)
admin.site.register(RAM)
admin.site.register(Storage)
