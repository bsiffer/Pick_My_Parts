from part import Part

class Motherboard(Part):
    """Represents a motherboard with attributes related to architecture, size, and compatibility."""

    def __init__(self, manufacturer, name, sku, price, socket_type, form_factor, ram_slots, supported_ram_type):
        """Initializes a Motherboard instance."""
        super().__init__(manufacturer, name, sku, price)
        self.__socket_type = socket_type
        self.__form_factor = form_factor
        self.__ram_slots = ram_slots
        self.__supported_ram_type = supported_ram_type

    def get_socket_type(self):
        return self.__socket_type

    def set_socket_type(self, socket_type):
        self.__socket_type = socket_type

    def get_form_factor(self):
        return self.__form_factor

    def set_form_factor(self, form_factor):
        self.__form_factor = form_factor

    def get_ram_slots(self):
        return self.__ram_slots

    def set_ram_slots(self, ram_slots):
        self.__ram_slots = ram_slots

    def get_supported_ram_type(self):
        return self.__supported_ram_type

    def set_supported_ram_type(self, ram_type):
        self.__supported_ram_type = ram_type

    def check_compatibility(self, parts_list):
        """Checks the compatibility of the motherboard with the CPU and RAM in the parts list."""
        issues = []

        cpu = parts_list.get_part("CPU")
        if cpu:
            if cpu.get_socket_type() != self.__socket_type:
                issues.append(f"Motherboard socket ({self.__socket_type}) does not match CPU socket ({cpu.get_socket_type()}).")

        ram = parts_list.get_part("RAM")
        if ram:
            if ram.get_ram_type() != self.__supported_ram_type:
                issues.append(f"Motherboard supports {self.__supported_ram_type}, but selected RAM is {ram.get_ram_type()}.")

        return issues

    def to_string(self):
        """Returns a string representation of the motherboard."""
        base_info = super().to_string()
        return (f"{base_info}\nSocket Type: {self.__socket_type}, Form Factor: {self.__form_factor}, "
                f"RAM Slots: {self.__ram_slots}, Supported RAM Type: {self.__supported_ram_type}")
