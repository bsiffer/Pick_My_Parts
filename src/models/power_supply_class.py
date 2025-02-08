# power supply class inheriting from part.py
from models.part_class import Part

class PowerSupply(Part):
    def __init__(self, manufacturer, part_name, sku, price, size_standard, rated_wattage, certification_level, modular, efficiency_rating_percentage, pcie_connectors, length):
        super().__init__(manufacturer, part_name, sku, price)
        self.size_standard = size_standard  # stores size standard like atx, sfx
        self.rated_wattage = rated_wattage  # stores wattage rating like 750w
        self.certification_level = certification_level  # stores efficiency rating like 80+ gold
        self.modular = modular  # stores whether psu is modular, semi-modular, or non-modular
        self.efficiency_rating_percentage = efficiency_rating_percentage  # used to determine how much power is effectively converted
        self.pcie_connectors = pcie_connectors  # stores number of pcie power connectors available
        self.length = length  # stores the length of the psu to check for case compatibility

    def display_info(self):
        # returns a formatted string with power supply details
        base_info = super().display_info()
        return (f"{base_info}\nSize: {self.size_standard}, Wattage: {self.rated_wattage}W, "
                f"Certification: {self.certification_level}, Modular: {self.modular}, "
                f"Efficiency Rating: {self.efficiency_rating_percentage}%, PCIe Connectors: {self.pcie_connectors}, "
                f"Length: {self.length}mm")
    