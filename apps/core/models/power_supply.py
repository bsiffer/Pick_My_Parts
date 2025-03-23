from django.db import models
from apps.core.models.part import Part

class PowerSupply(Part, models.Model):
    size_standard = models.CharField(max_length=255)
    rated_wattage = models.DecimalField(max_digits=10, decimal_places=2)
    certification_level = models.CharField(max_length=255)
    modular = models.CharField(max_length=255)
    efficiency_rating_percentage = models.DecimalField(max_digits=3, decimal_places=2)
    pcie_connectors = models.IntegerField()
    length_in_mm = models.IntegerField()

    def check_compatibility(self, parts_list):
        pass

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
            f"Length: {self.length}mm"
        )