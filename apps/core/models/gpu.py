from django.db import models
from apps.core.models.part import Part
from apps.core.models.motherboard import Motherboard 

class GPU(Part, models.Model):
    """
    Represents a GPU with attributes related to performance, power, and compatibility.
    """
    architecture = models.CharField(max_length=255)
    memory_bus = models.IntegerField()
    pcie_standard = models.CharField(max_length=255)
    slot_size = models.CharField(max_length=255)
    length_in_mm = models.DecimalField(max_digits=10, decimal_places=2)
    cooling_type = models.CharField(max_length=255)
    power_requirement = models.DecimalField(max_digits=10, decimal_places=2)
    power_connectors = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    def check_compatibility(self, parts_list):
        """
        Checks if this GPU is compatible with the motherboard in the parts list.
        Currently checks PCIe standard compatibility.
        """
        motherboard = None

        for part in parts_list:
            if isinstance(part, Motherboard):
                motherboard = part
                break

        if not motherboard:
            return False  # No motherboard to compare with
   
        gpu_pcie = self.pcie_standard.lower().replace("pcie ", "")
        mobo_chipset = motherboard.chipset_compatibility.lower()

        if gpu_pcie not in mobo_chipset:
            return False

        return True

    def __str__(self):
        """Returns a string representation of the GPU."""
        base_info = super().__str__()
        return (
            f"{base_info}\nArchitecture: {self.architecture}\n"
            f"Memory Bus: {self.memory_bus}-bit\n"
            f"PCIe Standard: {self.pcie_standard}\n"
            f"Slot Size: {self.slot_size}\n"
            f"Length: {self.length_in_mm}mm\n"
            f"Cooling Type: {self.cooling_type}\n"
            f"Power Requirement: {self.power_requirement}W\n"
            f"Power Connectors: {self.power_connectors}\n"
            f"Color: {self.color}"
        )