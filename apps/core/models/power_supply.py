from django.db import models
from apps.core.models.part import Part

class PowerSupply(Part, models.Model):
    size_standard = models.CharField(max_length=255)
    rated_wattage = models.DecimalField(max_digits=10, decimal_places=2)
    certification_level = models.CharField(max_length=255)
    modular = models.CharField(max_length=255)
    efficiency_rating_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    pcie_connectors = models.IntegerField()
    length_in_mm = models.IntegerField()

    def check_compatibility(self, parts_list):
        issues = []
        total_power = 0.0

        cpus = parts_list.parts.get("CPU", [])
        gpus = parts_list.parts.get("GPU", [])

        if len(cpus) == 1:
            # Assume only one CPU can be selected
            cpu = cpus[0]
            total_power += float(cpu.wattage_compatibility)

        if len(gpus) == 1:
            # Assume only one GPU can be selected
            gpu = gpus[0]
            total_power += float(gpu.power_requirement)

        if total_power > float(self.rated_wattage) * .75:  # Multiplied by 75% to allow overhead for other components
            issues.append(
                f"Power supply '{self.get_name()}' rated at {self.rated_wattage}W may be insufficient for the total power requirement ({total_power}W)."
            )
        return issues

    def __str__(self):
        """Returns a string representation of the power supply."""
        base_info = super().__str__()
        return (
            f"{base_info}\n"
            f"Size Standard: {self.size_standard}\n"
            f"Wattage: {self.rated_wattage}W\n"
            f"Certification: {self.certification_level}\n"
            f"Modular: {self.modular}\n"
            f"Efficiency Rating: {self.efficiency_rating_percentage}%\n"
            f"PCIe Connectors: {self.pcie_connectors}\n"
            f"Length: {self.length_in_mm}mm"
        )