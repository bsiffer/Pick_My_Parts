from django.db import models
from apps.core.models.part import Part

class CoolingAccessory(Part, models.Model):
    cooling_type = models.CharField(max_length=255)
    supported_sockets = models.JSONField(default=list)

    def check_compatibility(self, parts_list):
        """
        Checks if the cooling accessory is compatible with a CPU and a computer case.
        Compatibility is based on:
        - CPU socket type (must be in the cooler's supported_sockets)
        - Case form factor must support the cooling type (AIR, Liquid, AIO)
        """
        issues = []
        cpus = parts_list.parts.get("CPU", [])
        computer_cases = parts_list.parts.get("ComputerCase", [])

        if len(cpus) == 1:
            # Assume only one CPU can be selected
            cpu = cpus[0]
            # Check socket compatibility
            if cpu.socket_type not in self.supported_sockets:
                issues.append(
                    f"{self.get_name()} is incompatible: CPU socket type {cpu.socket_type} is not supported by the cooling accessory."
                )

        if len(computer_cases) == 1:
            # Assume only one computer case can be selected
            computer_case = computer_cases[0]
            if self.cooling_type not in computer_case.supported_cooling_types:
                issues.append(
                    f"{self.get_name()} is incompatible: Cooling type {self.cooling_type} is not supported by the computer case."
                )

        return issues

    def __str__(self):
        """Returns a string representation of the cooling accessory."""
        base_info = super().__str__()
        return f"{base_info}\nCooling Type: {self.cooling_type}"