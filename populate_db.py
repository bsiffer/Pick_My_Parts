import os
import django

# Set up Django environment
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

# Create sample FormFactors (if they don't exist)
ff_names = ["ATX", "Micro-ATX", "Mini-ITX", "E-ATX", "BTX"]
form_factors = {}
for name in ff_names:
    ff, created = FormFactor.objects.get_or_create(name=name)
    form_factors[name] = ff

# Create sample CPUs
cpus_data = [
    {
        "manufacturer": "Intel",
        "name": "Core i9-12900K",
        "sku": 100001,
        "price": 589.99,
        "architecture": "Alder Lake",
        "clock_speed": 3.2,
        "ddr4_compatibility": True,
        "ddr5_compatibility": True,
        "socket_type": "LGA1700",
        "wattage_compatibility": 125.0,
        "bios_compatibility": True,
        "chipset_compatibility": True
    },
    {
        "manufacturer": "AMD",
        "name": "Ryzen 9 5950X",
        "sku": 100002,
        "price": 799.99,
        "architecture": "Zen 3",
        "clock_speed": 3.4,
        "ddr4_compatibility": True,
        "ddr5_compatibility": False,
        "socket_type": "AM4",
        "wattage_compatibility": 105.0,
        "bios_compatibility": True,
        "chipset_compatibility": True
    },
    {
        "manufacturer": "Intel",
        "name": "Core i7-12700K",
        "sku": 100003,
        "price": 409.99,
        "architecture": "Alder Lake",
        "clock_speed": 3.6,
        "ddr4_compatibility": True,
        "ddr5_compatibility": True,
        "socket_type": "LGA1700",
        "wattage_compatibility": 125.0,
        "bios_compatibility": True,
        "chipset_compatibility": True
    },
    {
        "manufacturer": "AMD",
        "name": "Ryzen 7 5800X",
        "sku": 100004,
        "price": 449.99,
        "architecture": "Zen 3",
        "clock_speed": 3.8,
        "ddr4_compatibility": True,
        "ddr5_compatibility": False,
        "socket_type": "AM4",
        "wattage_compatibility": 105.0,
        "bios_compatibility": True,
        "chipset_compatibility": True
    },
    {
        "manufacturer": "Intel",
        "name": "Core i5-12600K",
        "sku": 100005,
        "price": 299.99,
        "architecture": "Alder Lake",
        "clock_speed": 3.7,
        "ddr4_compatibility": True,
        "ddr5_compatibility": True,
        "socket_type": "LGA1700",
        "wattage_compatibility": 125.0,
        "bios_compatibility": True,
        "chipset_compatibility": True
    },
]
for data in cpus_data:
    CPU.objects.create(**data)

# Create sample GPUs
gpus_data = [
    {
        "manufacturer": "NVIDIA",
        "name": "RTX 3080",
        "sku": 200001,
        "price": 699.99,
        "architecture": "Ampere",
        "memory_bus": 320,
        "pcie_standard": "PCIe 4.0",
        "slot_size": "2-Slot",
        "length_in_mm": 285.0,
        "cooling_type": "Air",
        "power_requirement": 320.0,
        "power_connectors": "2x8-pin",
        "color": "Black"
    },
    {
        "manufacturer": "AMD",
        "name": "Radeon RX 6800 XT",
        "sku": 200002,
        "price": 649.99,
        "architecture": "RDNA 2",
        "memory_bus": 256,
        "pcie_standard": "PCIe 4.0",
        "slot_size": "2-Slot",
        "length_in_mm": 267.0,
        "cooling_type": "Air",
        "power_requirement": 300.0,
        "power_connectors": "2x8-pin",
        "color": "Black"
    },
    {
        "manufacturer": "NVIDIA",
        "name": "RTX 3070",
        "sku": 200003,
        "price": 499.99,
        "architecture": "Ampere",
        "memory_bus": 256,
        "pcie_standard": "PCIe 4.0",
        "slot_size": "2-Slot",
        "length_in_mm": 242.0,
        "cooling_type": "Air",
        "power_requirement": 220.0,
        "power_connectors": "1x8-pin",
        "color": "White"
    },
    {
        "manufacturer": "AMD",
        "name": "Radeon RX 6700 XT",
        "sku": 200004,
        "price": 479.99,
        "architecture": "RDNA 2",
        "memory_bus": 192,
        "pcie_standard": "PCIe 4.0",
        "slot_size": "2-Slot",
        "length_in_mm": 267.0,
        "cooling_type": "Air",
        "power_requirement": 230.0,
        "power_connectors": "1x8-pin",
        "color": "Black"
    },
    {
        "manufacturer": "NVIDIA",
        "name": "RTX 3060",
        "sku": 200005,
        "price": 329.99,
        "architecture": "Ampere",
        "memory_bus": 192,
        "pcie_standard": "PCIe 4.0",
        "slot_size": "2-Slot",
        "length_in_mm": 242.0,
        "cooling_type": "Air",
        "power_requirement": 170.0,
        "power_connectors": "1x8-pin",
        "color": "Black"
    },
]
for data in gpus_data:
    GPU.objects.create(**data)

# Create sample Motherboards
motherboards_data = [
    {
        "manufacturer": "ASUS",
        "name": "ROG STRIX Z690-E",
        "sku": 300001,
        "price": 399.99,
        "socket_type": "LGA1700",
        "form_factor": "ATX",
        "ram_slots": 4,
        "supported_ram_type": "DDR5",
        "chipset_compatibility": "Z690",
        "bios_compatibility": "UEFI"
    },
    {
        "manufacturer": "MSI",
        "name": "MPG B550 Gaming Edge",
        "sku": 300002,
        "price": 179.99,
        "socket_type": "AM4",
        "form_factor": "ATX",
        "ram_slots": 4,
        "supported_ram_type": "DDR4",
        "chipset_compatibility": "B550",
        "bios_compatibility": "UEFI"
    },
    {
        "manufacturer": "Gigabyte",
        "name": "AORUS Elite",
        "sku": 300003,
        "price": 149.99,
        "socket_type": "AM4",
        "form_factor": "Micro-ATX",
        "ram_slots": 4,
        "supported_ram_type": "DDR4",
        "chipset_compatibility": "B450",
        "bios_compatibility": "UEFI"
    },
    {
        "manufacturer": "ASRock",
        "name": "Z690 Phantom Gaming",
        "sku": 300004,
        "price": 299.99,
        "socket_type": "LGA1700",
        "form_factor": "ATX",
        "ram_slots": 4,
        "supported_ram_type": "DDR5",
        "chipset_compatibility": "Z690",
        "bios_compatibility": "UEFI"
    },
    {
        "manufacturer": "EVGA",
        "name": "Z490 FTW",
        "sku": 300005,
        "price": 249.99,
        "socket_type": "LGA1200",
        "form_factor": "ATX",
        "ram_slots": 4,
        "supported_ram_type": "DDR4",
        "chipset_compatibility": "Z490",
        "bios_compatibility": "UEFI"
    },
]
for data in motherboards_data:
    Motherboard.objects.create(**data)

# Create sample Power Supplies
power_supplies_data = [
    {
        "manufacturer": "Corsair",
        "name": "RM850x",
        "sku": 400001,
        "price": 129.99,
        "size_standard": "ATX",
        "rated_wattage": 850.00,
        "certification_level": "80 PLUS Gold",
        "modular": "Fully Modular",
        "efficiency_rating_percentage": 90.00,
        "pcie_connectors": 4,
        "length_in_mm": 160
    },
    {
        "manufacturer": "EVGA",
        "name": "SuperNOVA 750 G5",
        "sku": 400002,
        "price": 119.99,
        "size_standard": "ATX",
        "rated_wattage": 750.00,
        "certification_level": "80 PLUS Gold",
        "modular": "Fully Modular",
        "efficiency_rating_percentage": 89.00,
        "pcie_connectors": 3,
        "length_in_mm": 150
    },
    {
        "manufacturer": "Seasonic",
        "name": "Focus GX-650",
        "sku": 400003,
        "price": 99.99,
        "size_standard": "ATX",
        "rated_wattage": 650.00,
        "certification_level": "80 PLUS Gold",
        "modular": "Fully Modular",
        "efficiency_rating_percentage": 88.00,
        "pcie_connectors": 2,
        "length_in_mm": 140
    },
    {
        "manufacturer": "Cooler Master",
        "name": "MWE Gold 750",
        "sku": 400004,
        "price": 109.99,
        "size_standard": "ATX",
        "rated_wattage": 750.00,
        "certification_level": "80 PLUS Gold",
        "modular": "Semi-Modular",
        "efficiency_rating_percentage": 87.00,
        "pcie_connectors": 3,
        "length_in_mm": 150
    },
    {
        "manufacturer": "Thermaltake",
        "name": "Smart 600W",
        "sku": 400005,
        "price": 69.99,
        "size_standard": "ATX",
        "rated_wattage": 600.00,
        "certification_level": "80 PLUS",
        "modular": "Non-Modular",
        "efficiency_rating_percentage": 85.00,
        "pcie_connectors": 1,
        "length_in_mm": 130
    },
]
for data in power_supplies_data:
    PowerSupply.objects.create(**data)

# Create sample RAM modules
rams_data = [
    {
        "manufacturer": "Corsair",
        "name": "Vengeance LPX 16GB",
        "sku": 500001,
        "price": 79.99,
        "capacity_in_gb": 16,
        "ddr_standard": "DDR4",
        "speed_in_mhz": 3200,
        "sticks": 2,
        "latency": "CL16",
        "rgb": False,
        "color": "Black"
    },
    {
        "manufacturer": "G.Skill",
        "name": "Trident Z RGB 16GB",
        "sku": 500002,
        "price": 89.99,
        "capacity_in_gb": 16,
        "ddr_standard": "DDR4",
        "speed_in_mhz": 3600,
        "sticks": 2,
        "latency": "CL16",
        "rgb": True,
        "color": "Black"
    },
    {
        "manufacturer": "Kingston",
        "name": "HyperX Fury 16GB",
        "sku": 500003,
        "price": 74.99,
        "capacity_in_gb": 16,
        "ddr_standard": "DDR4",
        "speed_in_mhz": 2666,
        "sticks": 2,
        "latency": "CL15",
        "rgb": False,
        "color": "Black"
    },
    {
        "manufacturer": "Patriot",
        "name": "Viper Steel 16GB",
        "sku": 500004,
        "price": 69.99,
        "capacity_in_gb": 16,
        "ddr_standard": "DDR4",
        "speed_in_mhz": 3000,
        "sticks": 2,
        "latency": "CL15",
        "rgb": False,
        "color": "Black"
    },
    {
        "manufacturer": "Crucial",
        "name": "Ballistix 16GB",
        "sku": 500005,
        "price": 84.99,
        "capacity_in_gb": 16,
        "ddr_standard": "DDR4",
        "speed_in_mhz": 3200,
        "sticks": 2,
        "latency": "CL16",
        "rgb": True,
        "color": "Black"
    },
]
for data in rams_data:
    RAM.objects.create(**data)

# Create sample Storage devices
storages_data = [
    {
        "manufacturer": "Samsung",
        "name": "970 EVO Plus 1TB",
        "sku": 600001,
        "price": 149.99,
        "storage_type": "NVMe SSD",
        "capacity_in_GB": 1000,
        "interface": "PCIe 3.0 x4"
    },
    {
        "manufacturer": "Western Digital",
        "name": "Blue 1TB",
        "sku": 600002,
        "price": 49.99,
        "storage_type": "SATA SSD",
        "capacity_in_GB": 1000,
        "interface": "SATA III"
    },
    {
        "manufacturer": "Seagate",
        "name": "Barracuda 2TB",
        "sku": 600003,
        "price": 59.99,
        "storage_type": "HDD",
        "capacity_in_GB": 2000,
        "interface": "SATA III"
    },
    {
        "manufacturer": "Crucial",
        "name": "MX500 500GB",
        "sku": 600004,
        "price": 64.99,
        "storage_type": "SATA SSD",
        "capacity_in_GB": 500,
        "interface": "SATA III"
    },
    {
        "manufacturer": "ADATA",
        "name": "XPG SX8200 Pro 1TB",
        "sku": 600005,
        "price": 139.99,
        "storage_type": "NVMe SSD",
        "capacity_in_GB": 1000,
        "interface": "PCIe 3.0 x4"
    },
]
for data in storages_data:
    Storage.objects.create(**data)

# Create sample Computer Cases
cases_data = [
    {
        "manufacturer": "NZXT",
        "name": "H510",
        "sku": 700001,
        "price": 69.99,
        "form_factor": form_factors["ATX"],
        "color": "Black"
    },
    {
        "manufacturer": "Corsair",
        "name": "Obsidian 500D",
        "sku": 700002,
        "price": 149.99,
        "form_factor": form_factors["ATX"],
        "color": "White"
    },
    {
        "manufacturer": "Phanteks",
        "name": "Eclipse P400A",
        "sku": 700003,
        "price": 79.99,
        "form_factor": form_factors["ATX"],
        "color": "Black"
    },
    {
        "manufacturer": "Cooler Master",
        "name": "MasterBox Q300L",
        "sku": 700004,
        "price": 39.99,
        "form_factor": form_factors["Micro-ATX"],
        "color": "Black"
    },
    {
        "manufacturer": "Fractal Design",
        "name": "Define 7",
        "sku": 700005,
        "price": 129.99,
        "form_factor": form_factors["ATX"],
        "color": "Black"
    },
]
for data in cases_data:
    case = ComputerCase.objects.create(**data)
    # Set supported form factors for each case
    case.supported_form_factors.set([data["form_factor"], form_factors["Micro-ATX"]])

# Create sample Cooling Accessories
cooling_accessories_data = [
    {
        "manufacturer": "Noctua",
        "name": "NH-D15",
        "sku": 800001,
        "price": 89.99,
        "cooling_type": "Air"
    },
    {
        "manufacturer": "Corsair",
        "name": "H100i",
        "sku": 800002,
        "price": 119.99,
        "cooling_type": "Liquid"
    },
    {
        "manufacturer": "be quiet!",
        "name": "Dark Rock Pro 4",
        "sku": 800003,
        "price": 89.99,
        "cooling_type": "Air"
    },
    {
        "manufacturer": "Cooler Master",
        "name": "MasterLiquid ML240L",
        "sku": 800004,
        "price": 99.99,
        "cooling_type": "Liquid"
    },
    {
        "manufacturer": "NZXT",
        "name": "Kraken X53",
        "sku": 800005,
        "price": 109.99,
        "cooling_type": "Liquid"
    },
]
for data in cooling_accessories_data:
    CoolingAccessory.objects.create(**data)

print("Database populated successfully!")
