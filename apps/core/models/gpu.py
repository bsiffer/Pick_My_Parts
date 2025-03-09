from part import Part

class Gpu(Part):
    """Represents a GPU with attributes related to performance, power, and compatibility."""

    def __init__(self, manufacturer, name, sku, price, architecture, memory_bus, pcie_standard, slot_size,
                 length, cooling_type, power_requirement, power_connectors, color):
        """Initializes a Gpu instance."""
        super().__init__(manufacturer, name, sku, price)
        self.__architecture = architecture
        self.__memory_bus = memory_bus
        self.__pcie_standard = pcie_standard
        self.__slot_size = slot_size
        self.__length = length
        self.__cooling_type = cooling_type
        self.__power_requirement = power_requirement
        self.__power_connectors = power_connectors
        self.__color = color

    def get_architecture(self):
        return self.__architecture

    def set_architecture(self, architecture):
        self.__architecture = architecture

    def get_memory_bus(self):
        return self.__memory_bus

    def set_memory_bus(self, memory_bus):
        self.__memory_bus = memory_bus

    def get_pcie_standard(self):
        return self.__pcie_standard

    def set_pcie_standard(self, pcie_standard):
        self.__pcie_standard = pcie_standard

    def get_slot_size(self):
        return self.__slot_size

    def set_slot_size(self, slot_size):
        self.__slot_size = slot_size

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_cooling_type(self):
        return self.__cooling_type

    def set_cooling_type(self, cooling_type):
        self.__cooling_type = cooling_type

    def get_power_requirement(self):
        return self.__power_requirement

    def set_power_requirement(self, power_requirement):
        self.__power_requirement = power_requirement

    def get_power_connectors(self):
        return self.__power_connectors

    def set_power_connectors(self, power_connectors):
        self.__power_connectors = power_connectors

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def check_compatibility(self, parts_list):
        """Checks GPU compatibility with the power supply and case."""
        issues = []

        # Check power supply compatibility
        psu = parts_list.get_part("PowerSupply")
        if psu:
            if psu.get_rated_wattage() < self.__power_requirement:
                issues.append(f"GPU requires {self.__power_requirement}W, but PSU provides only {psu.get_rated_wattage()}W.")
            if psu.get_pcie_connectors() < int(self.__power_connectors):
                issues.append(f"GPU requires {self.__power_connectors} PCIe connectors, but PSU provides only {psu.get_pcie_connectors()}.")

        # Check case compatibility
        case = parts_list.get_part("ComputerCase")
        if case:
            if self.__length > case.get_length():
                issues.append(f"GPU length ({self.__length}mm) exceeds the case's maximum supported length ({case.get_length()}mm).")
            if self.__slot_size > case.get_slot_capacity():
                issues.append(f"GPU requires {self.__slot_size} expansion slots, but case only supports {case.get_slot_capacity()}.")

        return issues

    def to_string(self):
        """Returns a string representation of the GPU."""
        base_info = super().to_string()
        return (f"{base_info}\nArchitecture: {self.__architecture}\n"
                f"Memory Bus: {self.__memory_bus}-bit\n"
                f"PCIe Standard: {self.__pcie_standard}\n"
                f"Slot Size: {self.__slot_size}\n"
                f"Length: {self.__length}mm\n"
                f"Cooling Type: {self.__cooling_type}\n"
                f"Power Requirement: {self.__power_requirement}W\n"
                f"Power Connectors: {self.__power_connectors}\n"
                f"Color: {self.__color}")
