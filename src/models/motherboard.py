""" Motherboard class inheriting from part.py """
from src.models.part import Part
from src.utils.parts_compatibility_manager import check_storage_motherboard

class Motherboard(Part):
    def __init__(self, manufacturer, name, sku, price, architecture, standard_size, ram_slots, compatibility):
        super().__init__(manufacturer, name, sku, price)
        self.architecture = architecture  # e.g., x86, ARM
        self.standard_size = standard_size  # e.g., ATX, Micro-ATX, Mini-ITX
        self.ram_slots = ram_slots  # Number of RAM slots
        self.compatibility = compatibility  # List of compatible CPUs, RAM types, etc.

    def is_compatible_with(self, part):
        """Checks if the given part is compatible with the motherboard."""
        if isinstance(part, Ram):
            return part.get_ddr_standard() in self.compatibility
        elif isinstance(part, Storage):
            return check_storage_motherboard(part, self)  # Using compatibility manager
        return True  # Default to True for other parts

    def to_string(self):
        base_info = super().to_string()
        return (f"{base_info}\nArchitecture: {self.architecture}, Size: {self.standard_size}, "
                f"RAM Slots: {self.ram_slots}, Compatibility: {self.compatibility}")
