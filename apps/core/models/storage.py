from django.db import models
from apps.core.models.part import Part

class Storage(Part, models.Model):
    storage_type = models.CharField(max_length=255)
    capacity_in_GB = models.IntegerField()
    interface = models.CharField(max_length=255)

    def check_compatibility(self, parts_list):
        pass

    def __str__(self):
        """Returns a string representation of the storage device."""
        base_info = super().__str__()
        return (
            f"{base_info}\nType: {self.storage_type}\n"
            f"Capacity: {self.capacity_in_GB}GB\n"
            f"Interface: {self.interface}"
        )