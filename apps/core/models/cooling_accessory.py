from django.db import models
from apps.core.models.part import Part
from apps.core.models.cpu import CPU
from apps.core.models.computer_case import ComputerCase

class CoolingAccessory(Part, models.Model):
    cooling_type = models.CharField(max_length=255)

    def check_compatibility(self, parts_list):
        """
        Checks if the cooling accessory is compatible with a CPU and a computer case.
        Compatibility is based on:
        - CPU socket type (must be in the cooler's supported_sockets)
        - Case form factor must support the cooling type (AIR, Liquid, AIO)
        """
        cpu = None
        computer_case = None

        for part in parts_list:
            if isinstance(part, CPU):
                cpu = part
            elif isinstance(part, ComputerCase):
                computer_case = part

        if not cpu or not computer_case:
            return False

        # Check socket compatibility
        if cpu.socket_type not in self.supported_sockets:
            return False

        if not hasattr(computer_case, "supported_cooling_types"):
            return False

        if self.cooling_type not in computer_case.supported_cooling_types():
            return False

        return True

    def __str__(self):
        """Returns a string representation of the cooling accessory."""
        base_info = super().__str__()
        return f"{base_info}\nCooling Type: {self.cooling_type}"