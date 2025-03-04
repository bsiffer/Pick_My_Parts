from ..models.part import Part


class Gpu(Part):
    def __init__(self, manufacturer: str, name: str, sku: int, price: float, architecture: str,
                 memory_bus: int, pcie_standard: int, slot_size: int, length: int, cooling_type: str,
                 power_requirement: int, power_connectors: str, color: str) -> None:

        super().__init__(manufacturer, name, sku, price)
        self.__architecture = architecture  # Defines the GPU architecture
        self.__memory_bus = memory_bus  # Defines the bit size for memory bus
        self.__pcie_standard = pcie_standard  # Defines the PCIe standard for card
        self.__slot_size = slot_size  # Defines the amount of case slots that card uses
        self.__length = length  # Defines the length of gpu card and cooler
        self.__cooling_type = cooling_type  # Defines the cooling type on card
        self.__power_requirement = power_requirement  # Defines the power in watts required for the card
        self.__power_connectors = power_connectors  # Defines the type of power delivery needed
        self.__color = color  # Defines the majority color of the card and cooler

    # Get and set methods for each GPU attribute
    def get_architecture(self) -> str:
        return self.__architecture

    def set_architecture(self, architecture: str) -> None:
        self.__architecture = architecture

    def get_memory_bus(self) -> int:
        return self.__memory_bus

    def set_memory_bus(self, memory_bus: int) -> None:
        self.__memory_bus = memory_bus

    def get_pcie_standard(self) -> int:
        return self.__pcie_standard

    def set_pcie_standard(self, pcie_standard: int) -> None:
        self.__pcie_standard = pcie_standard

    def get_slot_size(self) -> int:
        return self.__slot_size

    def set_slot_size(self, slot_size: int) -> None:
        self.__slot_size = slot_size

    def get_length(self) -> int:
        return self.__length

    def set_length(self, length: int) -> None:
        self.__length = length

    def get_cooling_type(self) -> str:
        return self.__cooling_type

    def set_cooling_type(self, cooling_type: str) -> None:
        self.__cooling_type = cooling_type

    def get_power_requirement(self) -> int:
        return self.__power_requirement

    def set_power_requirement(self, power_req: int) -> None:
        self.__power_requirement = power_req

    def get_power_connectors(self) -> str:
        return self.__power_connectors

    def set_power_connectors(self, power_connectors: str) -> None:
        self.__power_connectors = power_connectors

    def get_color(self) -> str:
        return self.__color

    def set_color(self, color: str) -> None:
        self.__color = color

    # Information display for GPU part
    def to_string(self):
        part_information = super().to_string()
        return (f'{part_information}\n'
              f'Part Name: {self.__name}\n'
              f'Price: {self.__price}\n'
              f'SKU: {self.__sku}\n'
              f'Manufacturer: {self.__manufacturer}\n'
              f'Architecture: {self.__architecture}\n'
              f'Memory Bus: {self.__memory_bus}\n'
              f'PCIe Standard: {self.__pcie_standard}\n'
              f'Slot Size: {self.__slot_size}\n '
              f'GPU Length: {self.__length}\n'
              f'Cooling Type: {self.__cooling_type}\n'
              f'Power Requirement: {self.__power_requirement}\n'
              f'Power Connectors: {self.__power_connectors}\n'
              f'Color: {self.__color}')
