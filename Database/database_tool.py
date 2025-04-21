import json
import os


def user_selection():
    print(
        "To add/remove a CPU part press 1.\n"
        "To add/remove a GPU part press 2.\n"
        "To add/remove a motherboard part press 3.\n"
        "To add/remove a storage part press 4.\n"
        "To add/remove a RAM part press 5.\n"
        "To add/remove a case part press 6.\n"
        "To add/remove a psu part press 7.\n"
        "To add/remove a cooling/accessory part press 8.\n"
        "To close this program press 9.\n"
    )
    user_input = input("Please select an option: ")
    match user_input:
        case "1":  # CPU
            user_input = input("Select 1 to add a CPU or select 2 to remove a CPU:")
            if user_input == "1":
                filename = "cpu_database.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": input("Please enter the SKU name: "),
                        "price": input("Please enter the part price: "),
                        "architecture": input("Please enter the CPU architecture: "),
                        "clock_speed": input("Please enter the base clock speed: "),
                        "ddr4_compatibility": input("Please enter 'Yes' or 'No' for DDR4 compatibility: "),
                        "ddr5_compatibility": input("Please enter 'Yes' or 'No' for DDR4 compatibility: "),
                        "socket_type": input("Please enter the CPU socket type: "),
                        "wattage_compatibility": input("Please enter the CPU's rated wattage: "),
                        "bios_compatibility": input("Please enter the CPU's bios type: "),
                        "chipset_compatibility": input("Please enter the CPU chipset type(s): ")}
                add_part(filename, data)
            else:
                selection_to_remove = input("Please enter the SKU to be removed from database: ")
                remove_part()
        case "2":  # GPU
            user_input = input("Select 1 to add a GPU or select 2 to remove a GPU:")
            if user_input == "1":
                filename = "gpu_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": input("Please enter the SKU name: "),
                        "price": input("Please enter the part price: "),
                        "architecture": input("Please enter the GUP architecture: "),
                        "memory_bus": input("Please input the Memory Bus size: "),
                        "pcie_standard": input("Please enter the PCIe standard: "),
                        "slot_size": input("Please enter the GPU slot size: "),
                        "length_in_mm": input("Please enter the GPU length in millimeters: "),
                        "cooling_type": input("Please enter the cooler type: "),
                        "power_requirement": input("Please enter the power requirement in wattage: "),
                        "power_connectors": input("Please enter the power connecor type: "),
                        "color": input("Please enter the GPU's main color: ")}
                add_part(filename, data)
            else:
                selection_to_remove = input("Please enter the SKU to be removed from database: ")
                remove_part()
        case "3":  # Motherboard
            user_input = input("Select 1 to add a Motherboard or select 2 to remove a Motherboard:")
            if user_input == "1":
                filename = "motherboard_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": input("Please enter the SKU name: "),
                        "price": input("Please enter the part price: "),
                        "socket_type": input("Please enter the motherboard socket type: "),
                        "form_factor": input("Please enter the motherboard's form factor: "),
                        "ram_slots": input("Please enter the number of RAM slots: "),
                        "supported_ram_type": input("Please enter the supported RAM type: "),
                        "chipset_compatibility": input("Please enter the motherboard's chipset: "),
                        "bios_compatibility": input("Please enter the motherboard's bios type: "),
                        "supported_storage_interfaces": input("Please enter the supported storage standards: "),
                        "supported_pcie_standards": input("Please enter the supported PCIe standard:")}
                add_part(filename, data)
            else:
                selection_to_remove = input("Please enter the SKU to be removed from database: ")
                remove_part()
        case "4":  # Storage
            user_input = input("Select 1 to add a Storage device or select 2 to remove a Storage device:")
            if user_input == "1":
                filename = "storage_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "), "sku": input("Please enter the SKU name: "),
                        "price": input("Please enter the part price: "),
                        "storage_type": input("Please enter the storage standard: "),
                        "capacity_in_GB": input("Please enter the storage capacity in GB or TB: "),
                        "interface": input("Please enter the storage interface type: ")}
                add_part(filename, data)
            else:
                selection_to_remove = input("Please enter the SKU to be removed from database: ")
                remove_part()
        case "5":  # RAM
            user_input = input("Select 1 to add RAM or select 2 to remove RAM:")
            if user_input == "1":
                filename = "ram_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "), "sku": input("Please enter the SKU name: "),
                        "price": input("Please enter the part price: "),
                        "capacity_in_gb": input("Please enter the total capacity in GB: "),
                        "ddr_standard": input("Please enter the DDR standard: "),
                        "speed_in_mhz": input("Please enter the speed in MHz: "),
                        "sticks": input("Please enter the number of sticks in the kit: "),
                        "latency": input("Please enter the CAS latency: "),
                        "rgb": input("Please select the RGB capability of the kit: "),
                        "color": input("Please enter the main color of the kit: ")}
                add_part(filename, data)
            else:
                selection_to_remove = input("Please enter the SKU to be removed from database: ")
                remove_part()
        case "6":  # Case
            user_input = input("Select 1 to add a Case or select 2 to remove a Case:")
            if user_input == "1":
                filename = "cases_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "), "sku": input("Please enter the SKU name: "),
                        "price": input("Please enter the part price: "),
                        "form_factor": input("Please enter the case's form factor: "),
                        "color": input("Please enter the case's main color: "),
                        "supported_cooling_types": input("Please enter the supported cooling types: ")}
                add_part(filename, data)
            else:
                selection_to_remove = input("Please enter the SKU to be removed from database: ")
                remove_part()
        case "7":  # Power Supply
            user_input = input("Select 1 to add a Power Supply or select 2 to remove a Power Supply:")
            if user_input == "1":
                filename = "power_supplies_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "), "sku": input("Please enter the SKU name: "),
                        "price": input("Please enter the part price: "),
                        "size_standard": input("Please enter the PSU size standard: "),
                        "rated_wattage": input("Please enter the PSU rated wattage"),
                        "certification_level": input("Please enter the PSU certification rating: "),
                        "modular": input("Please indicate if the PSU is modular: "),
                        "efficiency_rating_percentage": input("Please enter the rated efficiency in percentage: "),
                        "pcie_connectors": input("Please enter the number of PCIe connectors: "),
                        "length_in_mm": input("Please enter the PSU length in millimeters: ")}
                add_part(filename, data)
            else:
                selection_to_remove = input("Please enter the SKU to be removed from database: ")
                remove_part()
        case "8":  # Cooling and Accessories
            user_input = input("Select 1 to add a part or select 2 to remove a part:")
            if user_input == "1":
                filename = "cooling_accessories_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "), "sku": input("Please enter the SKU name: "),
                        "price": input("Please enter the part price: "),
                        "cooling_type": input("Please enter the cooling type: "),
                        "supported_sockets": input("Please enter the supported socket types: ")}
                add_part(filename, data)
            else:
                selection_to_remove = input("Please enter the SKU to be removed from database: ")
                remove_part()
        case "9":  # Exit Program
            exit(0)


def add_part(filename, data):
    if os.path.exists(filename):
        with open(filename, 'a') as json_file:
            json.dump(data, json_file, indent=4)
    else:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    print(f"JSON data written to {filename}")

    user_selection()


def remove_part(filename, sku):
    pass


if __name__ == '__main__':
    user_selection()
