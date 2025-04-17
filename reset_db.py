import os
import django

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.core.models.cpu import CPU
from apps.core.models.gpu import GPU
from apps.core.models.motherboard import Motherboard
from apps.core.models.power_supply import PowerSupply
from apps.core.models.ram import RAM
from apps.core.models.storage import Storage
from apps.core.models.computer_case import ComputerCase
from apps.core.models.cooling_accessory import CoolingAccessory
from apps.core.models.form_factor import FormFactor

# ordered the models so that dependent records are removed before their dependencies.
models_to_delete = [
    CPU,
    GPU,
    Motherboard,
    PowerSupply,
    RAM,
    Storage,
    ComputerCase,
    CoolingAccessory,
    FormFactor
]

for model in models_to_delete:
    count = model.objects.count()
    model.objects.all().delete()
    print(f"Deleted {count} instances of {model.__name__}")

print("Database cleared successfully!")
