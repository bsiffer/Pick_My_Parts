# CPU class inheriting from part.py
from src.models.part import Part


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
        # Compatibility to be determined later
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

    def Check_compatibility(self):
        pass  # To be implemented later
