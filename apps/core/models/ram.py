from part import Part

class Ram(Part):
    """Represents a RAM module with attributes for capacity, speed, and compatibility."""

    def __init__(self, manufacturer, name, sku, price, capacity, standard, speed, sticks, latency, rgb, color):
        """Initializes a Ram instance."""
        super().__init__(manufacturer, name, sku, price)
        self.__capacity = capacity
        self.__ddr_standard = standard
        self.__speed = speed
        self.__sticks = sticks
        self.__latency = latency
        self.__rgb = rgb
        self.__color = color

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_ddr_standard(self):
        return self.__ddr_standard

    def set_ddr_standard(self, ddr_standard):
        self.__ddr_standard = ddr_standard

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_sticks(self):
        return self.__sticks

    def set_sticks(self, sticks):
        self.__sticks = sticks

    def get_latency(self):
        return self.__latency

    def set_latency(self, latency):
        self.__latency = latency

    def get_rgb(self):
        return self.__rgb

    def set_rgb(self, rgb):
        self.__rgb = rgb

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def check_compatibility(self, parts_list):
        """Checks if the RAM is compatible with the selected motherboard."""
        issues = []

        motherboard = parts_list.get_part("Motherboard")
        if motherboard:
            if self.__ddr_standard != motherboard.get_supported_ram_type():
                issues.append(
                    f"Motherboard supports {motherboard.get_supported_ram_type()}, but selected RAM is {self.__ddr_standard}."
                )
            if self.__sticks > motherboard.get_ram_slots():
                issues.append(
                    f"Motherboard has {motherboard.get_ram_slots()} RAM slots, but {self.__sticks} sticks were selected."
                )

        return issues

    def to_string(self):
        """Returns a string representation of the RAM module."""
        base_info = super().to_string()
        return (f"{base_info}\nCapacity: {self.__capacity}GB\n"
                f"DDR Standard: {self.__ddr_standard}\n"
                f"Speed: {self.__speed}MHz\n"
                f"Sticks: {self.__sticks}\n"
                f"CAS Latency: {self.__latency}\n"
                f"RGB: {'Yes' if self.__rgb else 'No'}\n"
                f"Color: {self.__color}")
