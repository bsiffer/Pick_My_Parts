import os
import json
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Import models
from apps.core.models.cpu import CPU
from apps.core.models.gpu import GPU
from apps.core.models.motherboard import Motherboard
from apps.core.models.power_supply import PowerSupply
from apps.core.models.ram import RAM
from apps.core.models.storage import Storage
from apps.core.models.computer_case import ComputerCase
from apps.core.models.cooling_accessory import CoolingAccessory
from apps.core.models.form_factor import FormFactor

# Map JSON files to models
model_mapping = {
    "form_factor.json": FormFactor,
    "cpu.json": CPU,
    "gpu.json": GPU,
    "motherboard.json": Motherboard,
    "power_supply.json": PowerSupply,
    "ram.json": RAM,
    "storage.json": Storage,
    "computer_case.json": ComputerCase,
    "cooling_accessory.json": CoolingAccessory,
}


def populate_database(wipe_first=False):
    data_dir = os.path.join(os.path.dirname(__file__), 'data')

    if wipe_first:
        print("Wiping existing database entries...")
        FormFactor.objects.all().delete()
        CPU.objects.all().delete()
        GPU.objects.all().delete()
        Motherboard.objects.all().delete()
        PowerSupply.objects.all().delete()
        RAM.objects.all().delete()
        Storage.objects.all().delete()
        ComputerCase.objects.all().delete()
        CoolingAccessory.objects.all().delete()

    for filename, model in model_mapping.items():
        file_path = os.path.join(data_dir, filename)

        if not os.path.exists(file_path):
            print(f"Warning: {filename} not found, skipping...")
            continue

        with open(file_path, 'r') as json_file:
            try:
                items = json.load(json_file)
            except json.JSONDecodeError:
                print(f"Error decoding {filename}, skipping...")
                continue

        for item_data in items:
            # Handle Motherboard form_factor
            if model == Motherboard and 'form_factor' in item_data:
                try:
                    form_factor_obj = FormFactor.objects.get(name=item_data['form_factor'])
                    item_data['form_factor'] = form_factor_obj
                except FormFactor.DoesNotExist:
                    print(f"Warning: FormFactor '{item_data['form_factor']}' not found for motherboard '{item_data.get('name')}', skipping.")
                    continue

            # Handle ComputerCase form_factor and supported_form_factors
            if model == ComputerCase:
                supported_form_factors = item_data.pop('supported_form_factors', None)

                if 'form_factor' in item_data:
                    try:
                        form_factor_obj = FormFactor.objects.get(name=item_data['form_factor'])
                        item_data['form_factor'] = form_factor_obj
                    except FormFactor.DoesNotExist:
                        print(f"Warning: FormFactor '{item_data['form_factor']}' not found for case '{item_data.get('name')}', skipping.")
                        continue

            obj, created = model.objects.get_or_create(**item_data)

            if model == ComputerCase and supported_form_factors:
                form_factors = []
                for ff_name in supported_form_factors:
                    try:
                        ff_obj = FormFactor.objects.get(name=ff_name)
                        form_factors.append(ff_obj)
                    except FormFactor.DoesNotExist:
                        print(f"Warning: Supported FormFactor '{ff_name}' not found for case '{obj.name}', skipping that form factor.")
                obj.supported_form_factors.set(form_factors)
                obj.save()

            action = "Created" if created else "Already exists"
            print(f"{action}: {model.__name__} - {obj.name}")

    print("\nDatabase population complete.")


if __name__ == "__main__":
    wipe = input("Do you want to wipe the database before populating? (y/n): ").lower() == 'y'
    populate_database(wipe_first=wipe)
