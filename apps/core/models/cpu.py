# CPU class inheriting from part.py
from part import Part


class CPU(Part):
    # Constructor to create a CPU.
    def __init__(
        self,
        manufacturer: str,
        name: str,
        sku: int,
        price: float,
        architecture: str,
        clock_speed: float,
        ddr4_compatibility: bool,
        ddr5_compatibility: bool,
        socket_type: str,
        wattage_compatibility: float,
        bios_compatibility: str,
        chipset_compatibility: str,
    ):
        # Call super class constructor
        super().__init__(manufacturer, name, sku, price)
        self.__architecture = architecture
        self.__clock_speed = clock_speed
        self.__ddr4_compatibility = ddr4_compatibility
        self.__ddr5_compatibility = ddr5_compatibility
        self.__socket_type = socket_type
        self.__wattage_compatibility = wattage_compatibility
        self.__bios_compatibility = bios_compatibility
        self.__chipset_compatibility = chipset_compatibility

    # Getters and Setters for private variables __architecture and __clock_speed
    def get_architecture(self):
        return self.__architecture

    def get_clock_speed(self):
        return self.__clock_speed

    def get_ddr4_compatibility(self):
        return self.__ddr4_compatibility

    def get_ddr5_compatibility(self):
        return self.__ddr5_compatibility

    def get_socket_type(self):
        return self.__socket_type

    def get_wattage_compatibility(self):
        return self.__wattage_compatibility

    def get_bios_compatibility(self):
        return self.__bios_compatibility

    def get_chipset_compatibility(self):
        return self.__chipset_compatibility

    def set_architecture(self, architecture):
        self.__architecture = architecture

    def set_clock_speed(self, clock_speed):
        self.__clock_speed = clock_speed

    def set_ddr4_compatibility(self, ddr4_compatibility):
        self.__ddr4_compatibility = ddr4_compatibility

    def set_ddr5_compatibility(self, ddr5_compatibility):
        self.__ddr5_compatibility = ddr5_compatibility

    def set_socket_type(self, socket_type):
        self.__socket_type = socket_type

    def set_wattage_compatibility(self, wattage_compatibility):
        self.__wattage_compatibility = wattage_compatibility

    def set_bios_compatibility(self, bios_compatibility):
        self.__bios_compatibility = bios_compatibility

    def set_chipset_compatibility(self, chipset_compatibility):
        self.__chipset_compatibility = chipset_compatibility

    # Method to display part and CPU details.
    def to_string(self):
        return (
            super().to_string()
            + f"\nArchitecture: {self.__architecture}\nClock Speed: {self.__clock_speed}\n"
        )

    def check_compatibility(self, part_list):
        issues = []
        motherboard = part_list["Motherboard"]
        power_supply = part_list["PowerSupply"]
        ram = part_list["RAM"]

        if motherboard != []:  # Check if a motherboard is in the part list.
            if not self.__socket_type == part_list["motherboard"].get_socket_type():
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Motherboard {part_list['motherboard'].get_name()}"
                )
            if (
                not self.__bios_compatibility
                == part_list["motherboard"].get_bios_compatibility()
            ):
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Motherboard {part_list['motherboard'].get_name()}"
                )
            if (
                not self.__chipset_compatibility
                == part_list["motherboard"].get_chipset_compatibility()
            ):
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Motherboard {part_list['motherboard'].get_name()}"
                )
        else:
            issues.append("no motherboard selected")

        if power_supply != []:
            if (
                not self.__wattage_compatibility
                <= part_list["power_supply"].get_wattage()
            ):
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Power Supply {part_list['power_supply'].get_name()}"
                )
        else:
            issues.append("no power supply selected")

        if ram != []:  # Check if a RAM stick/sticks are in the part list.
            for ram in part_list["ram"]:
                if (
                    not self.__ddr4_compatibility
                    and ram.get_ddr_standard() == "DDR4"
                    or not self.__ddr5_compatibility
                    and ram.get_ddr_standard() == "DDR5"
                ):
                    issues.append(
                        f"CPU {self.get_name()} is not compatible with RAM {ram.get_name()}"
                    )
        else:
            issues.append("no ram selected")
        return issues
