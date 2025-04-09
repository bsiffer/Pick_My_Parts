from django.db import models
from apps.core.models.part import Part
from apps.core.models.motherboard import Motherboard 

class Storage(Part, models.Model):
    storage_type = models.CharField(max_length=255)
    capacity_in_GB = models.IntegerField()
    interface = models.CharField(max_length=255)

    def check_compatibility(self, parts_list):
        """
        Checks if this storage device is compatible with a motherboard in the parts list.
        Returns True if compatible, False otherwise.
        """
        for part in parts_list:
            if isinstance(part, Motherboard):
                return self.interface in part.supported_storage_interfaces
        return False
    
    def __str__(self):
        """Returns a string representation of the storage device."""
        base_info = super().__str__()
        return (
            f"{base_info}\nType: {self.storage_type}\n"
            f"Capacity: {self.capacity_in_GB}GB\n"
            f"Interface: {self.interface}"
        )