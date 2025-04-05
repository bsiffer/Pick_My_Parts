from django.db import models
from apps.core.models.part import Part

class CoolingAccessory(Part, models.Model):
    cooling_type = models.CharField(max_length=255)

    def check_compatibility(self, parts_list):
        pass

    def __str__(self):
        """Returns a string representation of the cooling accessory."""
        base_info = super().__str__()
        return f"{base_info}\nCooling Type: {self.cooling_type}"