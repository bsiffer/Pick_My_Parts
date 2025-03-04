from src.models.cooling import CoolingAccessory
from src.models.part import Part
from src.models.motherboard import Motherboard

class ComputerCase(Part):
    def __init__(self, manufacturer: str, name: str, sku: int, price: float, size: str, color: str, compatibility: list):
        super().__init__(manufacturer, name, sku, price)
        self.size = size
        self.color = color
        self.compatibility = compatibility
    
    def is_compatible(self, motherboard: Motherboard) -> bool:
        """
        Checks if the case is compatible with the given motherboard.
        :param motherboard: Motherboard object to check compatibility against
        """
        return motherboard.standard_size in self.compatibility
    
    def add_compatibility(self, motherboard_size: str):
        """
        Adds a new compatible motherboard size if not already present.
        
        :param motherboard_size: The motherboard size to add to the compatibility list
        """
        if motherboard_size not in self.compatibility:
            self.compatibility.append(motherboard_size)
    
    def remove_compatibility(self, motherboard_size: str):
        """
        Removes a motherboard size from compatibility list if present.
                """
        if motherboard_size in self.compatibility:
            self.compatibility.remove(motherboard_size)
    
    def is_cooling_compatible(self, cooling: CoolingAccessory) -> bool:
        """
        Checks if the case supports the given cooling accessory.
        :param cooling: CoolingAccessory object to check compatibility against
        :return: True if the cooling type is in the case's cooling compatibility list, False otherwise
        """
        return cooling.get_cooling_type() in self.compatibility
    
    def add_cooling_compatibility(self, cooling_type: str):
        """
        Adds a new cooling type compatibility if not already present.
        :param cooling_type: The cooling type to add to the compatibility list
        """
        if cooling_type not in self.compatibility:
            self.compatibility.append(cooling_type)
            
    def remove_cooling_compatibility(self, cooling_type: str):
        """
        Removes a cooling type from compatibility list if present.
        :param cooling_type: The cooling type to remove from the compatibility list
        """
        if cooling_type in self.compatibility:
            self.compatibility.remove(cooling_type)
    def to_string(self):
        base_info = super().to_string()
        return f"{base_info}\nSize: {self.size}, Color: {self.color}, Compatible with: {', '.join(self.compatibility)}"
    