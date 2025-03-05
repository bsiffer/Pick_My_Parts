# power supply class inheriting from part.py
from ..models.part import Part

class PowerSupply(Part):
    def __init__(self, manufacturer: str, name: str, sku: int, price: float, size_standard: str, 
                 rated_wattage: int, certification_level: str, modular: str, 
                 efficiency_rating_percentage: float, pcie_connectors: int, length: int) -> None:

        super().__init__(manufacturer, name, sku, price)
        self.__size_standard = size_standard  # defines physical size standard for case compatibility
        self.__rated_wattage = rated_wattage  # stores psu wattage to check power requirements
        self.__certification_level = certification_level  # efficiency certification for power consumption
        self.__modular = modular  # indicates if the psu is modular, semi-modular, non-modular
        self.__efficiency_rating_percentage = efficiency_rating_percentage  # determines energy conversion efficiency
        self.__pcie_connectors = pcie_connectors  # defines available pcie connectors for gpu compatibility
        self.__length = length  # used for checking fit within cases

    # getters
    def get_size_standard(self) -> str:
        return self.__size_standard

    def get_rated_wattage(self) -> int:
        return self.__rated_wattage

    def get_certification_level(self) -> str:
        return self.__certification_level

    def get_modular(self) -> str:
        return self.__modular

    def get_efficiency_rating_percentage(self) -> float:
        return self.__efficiency_rating_percentage

    def get_pcie_connectors(self) -> int:
        return self.__pcie_connectors

    def get_length(self) -> int:
        return self.__length

    # setters
    def set_size_standard(self, size_standard: str) -> None:
        self.__size_standard = size_standard

    def set_rated_wattage(self, rated_wattage: int) -> None:
        self.__rated_wattage = rated_wattage

    def set_certification_level(self, certification_level: str) -> None:
        self.__certification_level = certification_level

    def set_modular(self, modular: str) -> None:
        self.__modular = modular

    def set_efficiency_rating_percentage(self, efficiency_rating_percentage: float) -> None:
        self.__efficiency_rating_percentage = efficiency_rating_percentage

    def set_pcie_connectors(self, pcie_connectors: int) -> None:
        self.__pcie_connectors = pcie_connectors

    def set_length(self, length: int) -> None:
        self.__length = length

    def to_string(self) -> str:
        # return power supply details in a formatted string.
        base_info = super().to_string()
        return (f"{base_info}\n"
                f"size standard: {self.__size_standard}\n"
                f"wattage: {self.__rated_wattage}W\n"
                f"certification: {self.__certification_level}\n"
                f"modular: {self.__modular}\n"
                f"efficiency rating: {self.__efficiency_rating_percentage}%\n"
                f"pcie connectors: {self.__pcie_connectors}\n"
                f"length: {self.__length}mm")

