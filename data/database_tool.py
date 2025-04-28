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
            filename = "cpu.json"
            if user_input == "1":
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": int(input("Please enter the SKU name: ")),
                        "price": float(input("Please enter the part price: ")),
                        "architecture": input("Please enter the CPU architecture: "),
                        "clock_speed": float(input("Please enter the base clock speed: ")),
                        "ddr4_compatibility": input("Please enter 'Yes' or 'No' for DDR4 compatibility: ").strip().lower() == "yes",
                        "ddr5_compatibility": input("Please enter 'Yes' or 'No' for DDR5 compatibility: ").strip().lower() == "yes",
                        "socket_type": input("Please enter the CPU socket type: "),
                        "wattage_compatibility": float(input("Please enter the CPU's rated wattage: ")),
                        "bios_compatibility": input("Please enter 'Yes' or 'No' for BIOS compatibility: ").strip().lower() == "yes",
                        "chipset_compatibility": input("Please enter 'Yes' or 'No' for chipset compatibility: ").strip().lower() == "yes"}
                add_part(filename, data)
            else:
                user_input = input("Please enter the SKU to be removed from database: ")
                selection_to_remove = int(user_input)
                remove_part(filename, selection_to_remove)
        case "2":  # GPU
            user_input = input("Select 1 to add a GPU or select 2 to remove a GPU:")
            if user_input == "1":
                filename = "../Database/gpu_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": int(input("Please enter the SKU name: ")),
                        "price": float(input("Please enter the part price: ")),
                        "architecture": input("Please enter the GPU architecture: "),
                        "memory_bus": int(input("Please input the Memory Bus size: ")),
                        "pcie_standard": input("Please enter the PCIe standard: "),
                        "slot_size": input("Please enter the GPU slot size: "),
                        "length_in_mm": float(input("Please enter the GPU length in millimeters: ")),
                        "cooling_type": input("Please enter the cooler type: "),
                        "power_requirement": float(input("Please enter the power requirement in wattage: ")),
                        "power_connectors": input("Please enter the power connector type: "),
                        "color": input("Please enter the GPU's main color: ")}
                add_part(filename, data)
            else:
                user_input = input("Please enter the SKU to be removed from database: ")
                selection_to_remove = int(user_input)
                remove_part(filename, selection_to_remove)
        case "3":  # Motherboard
            user_input = input("Select 1 to add a Motherboard or select 2 to remove a Motherboard:")
            if user_input == "1":
                filename = "../Database/motherboard_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": int(input("Please enter the SKU name: ")),
                        "price": float(input("Please enter the part price: ")),
                        "socket_type": input("Please enter the motherboard socket type: "),
                        "form_factor": input("Please enter the motherboard's form factor: "),
                        "ram_slots": int(input("Please enter the number of RAM slots: ")),
                        "supported_ram_type": input("Please enter the supported RAM type: "),
                        "chipset_compatibility": input("Please enter the motherboard's chipset: "),
                        "bios_compatibility": input("Please enter the motherboard's bios type: "),
                        "supported_storage_interfaces": input("Please enter the supported storage standards: "),
                        "supported_pcie_standards": input("Please enter the supported PCIe standard: ")}
                add_part(filename, data)
            else:
                user_input = input("Please enter the SKU to be removed from database: ")
                selection_to_remove = int(user_input)
                remove_part(filename, selection_to_remove)
        case "4":  # Storage
            user_input = input("Select 1 to add a Storage device or select 2 to remove a Storage device:")
            if user_input == "1":
                filename = "../Database/storage_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": int(input("Please enter the SKU name: ")),
                        "price": float(input("Please enter the part price: ")),
                        "storage_type": input("Please enter the storage standard: "),
                        "capacity_in_GB": int(input("Please enter the storage capacity in GB: ")),
                        "interface": input("Please enter the storage interface type: ")}
                add_part(filename, data)
            else:
                user_input = input("Please enter the SKU to be removed from database: ")
                selection_to_remove = int(user_input)
                remove_part(filename, selection_to_remove)
        case "5":  # RAM
            user_input = input("Select 1 to add RAM or select 2 to remove RAM:")
            if user_input == "1":
                filename = "../Database/ram_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": int(input("Please enter the SKU name: ")),
                        "price": float(input("Please enter the part price: ")),
                        "capacity_in_gb": int(input("Please enter the total capacity in GB: ")),
                        "ddr_standard": input("Please enter the DDR standard: "),
                        "speed_in_mhz": int(input("Please enter the speed in MHz: ")),
                        "sticks": int(input("Please enter the number of sticks in the kit: ")),
                        "latency": input("Please enter the CAS latency: "),
                        "rgb": input("Please select the RGB capability of the kit (Yes/No): ").strip().lower() == "yes",
                        "color": input("Please enter the main color of the kit: ")}
                add_part(filename, data)
            else:
                user_input = input("Please enter the SKU to be removed from database: ")
                selection_to_remove = int(user_input)
                remove_part(filename, selection_to_remove)
        case "6":  # Case
            user_input = input("Select 1 to add a Case or select 2 to remove a Case:")
            if user_input == "1":
                filename = "../Database/cases_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": int(input("Please enter the SKU name: ")),
                        "price": float(input("Please enter the part price: ")),
                        "form_factor": input("Please enter the case's form factor: "),
                        "color": input("Please enter the case's main color: "),
                        "supported_cooling_types": input("Please enter the supported cooling types: ")}
                add_part(filename, data)
            else:
                user_input = input("Please enter the SKU to be removed from database: ")
                selection_to_remove = int(user_input)
                remove_part(filename, selection_to_remove)
        case "7":  # Power Supply
            user_input = input("Select 1 to add a Power Supply or select 2 to remove a Power Supply:")
            if user_input == "1":
                filename = "../Database/power_supplies_data.json"
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": int(input("Please enter the SKU name: ")),
                        "price": float(input("Please enter the part price: ")),
                        "size_standard": input("Please enter the PSU size standard: "),
                        "rated_wattage": float(input("Please enter the PSU rated wattage: ")),
                        "certification_level": input("Please enter the PSU certification rating: "),
                        "modular": input("Is the PSU modular? (Yes/No): ").strip().lower() == "yes",
                        "efficiency_rating_percentage": float(input("Please enter the rated efficiency in percentage: ")),
                        "pcie_connectors": int(input("Please enter the number of PCIe connectors: ")),
                        "length_in_mm": float(input("Please enter the PSU length in millimeters: "))}
                add_part(filename, data)
            else:
                selection_to_remove = int(input("Please enter the SKU to be removed from database: "))
                remove_part(filename, selection_to_remove)
        case "8":  # Cooling and Accessories
            user_input = input("Select 1 to add a part or select 2 to remove a part:")
            filename = "../Database/cooling_accessories_data.json"
            if user_input == "1":
                data = {"manufacturer": input("Please enter the manufacturer: "),
                        "name": input("Please enter the part name: "),
                        "sku": int(input("Please enter the SKU name: ")),
                        "price": float(input("Please enter the part price: ")),
                        "cooling_type": input("Please enter the cooling type: "),
                        "supported_sockets": input("Please enter the supported socket types: ")}
                add_part(filename, data)
            else:
                user_input = input("Please enter the SKU to be removed from database: ")
                selection_to_remove = int(user_input)
                remove_part(filename, selection_to_remove)
        case "9":  # Exit Program
            exit(0)


def add_part(filename, data):
    if os.path.exists(filename):
        with open(filename, 'r+') as json_file:
            lines = json_file.readlines()
            if lines:
                json_file.seek(0)
                json_file.truncate()
                json_file.writelines(lines[:-1])
        with open(filename, 'a') as json_file:
            json_file.write(",\n")
            json.dump(data, json_file, indent=4)
            json_file.write("\n]")
    else:
        with open(filename, 'w') as json_file:
            json_file.write("[\n")
            json.dump(data, json_file, indent=4)
            json_file.write("\n]")

    print(f"JSON data written to {filename}")

    user_selection()


def remove_part(filename, target_sku):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        for element in data:
            if element["sku"] == target_sku:
                data.remove(element)
                break

    for x in data:
        print(x)

    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    user_selection()


if __name__ == '__main__':
    user_selection()
