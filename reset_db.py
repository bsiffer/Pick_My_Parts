import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Import all models
from apps.core.models.cpu import CPU
from apps.core.models.gpu import GPU
from apps.core.models.motherboard import Motherboard
from apps.core.models.power_supply import PowerSupply
from apps.core.models.ram import RAM
from apps.core.models.storage import Storage
from apps.core.models.computer_case import ComputerCase
from apps.core.models.cooling_accessory import CoolingAccessory
from apps.core.models.form_factor import FormFactor

def wipe_database():
    print("Wiping database...")

    # Delete in proper order (dependent models first)
    CPU.objects.all().delete()
    GPU.objects.all().delete()
    Motherboard.objects.all().delete()
    PowerSupply.objects.all().delete()
    RAM.objects.all().delete()
    Storage.objects.all().delete()
    ComputerCase.objects.all().delete()
    CoolingAccessory.objects.all().delete()
    FormFactor.objects.all().delete()

    print("Database wipe complete.")

if __name__ == "__main__":
    confirm = input("Are you sure you want to wipe the entire database? (y/n): ").lower()
    if confirm == 'y':
        wipe_database()
    else:
        print("Operation canceled.")
