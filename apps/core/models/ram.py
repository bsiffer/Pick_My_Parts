from django.db import models
from apps.core.models.part import Part

class RAM(Part, models.Model):
    capacity_in_gb = models.IntegerField()
    ddr_standard = models.CharField(max_length=255)
    speed_in_mhz = models.IntegerField()
    sticks = models.IntegerField()
    latency = models.CharField(max_length=255)
    rgb = models.BooleanField()
    color = models.CharField(max_length=255)

    def check_compatibility(self, parts_list):
        pass

    def __str__(self):
        """Returns a string representation of the RAM module."""
        base_info = super().__str__()
        return (
            f"{base_info}\nCapacity: {self.capacity_in_gb}GB\n"
            f"DDR Standard: {self.ddr_standard}\n"
            f"Speed: {self.speed_in_mhz}MHz\n"
            f"Sticks: {self.sticks}\n"
            f"CAS Latency: {self.latency}\n"
            f"RGB: {'Yes' if self.rgb else 'No'}\n"
            f"Color: {self.color}"
        )