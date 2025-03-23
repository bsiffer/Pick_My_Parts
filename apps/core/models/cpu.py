from django.db import models
from apps.core.models.part import Part

class CPU(Part, models.Model):
    architecture = models.CharField(max_length=255)
    clock_speed = models.DecimalField(max_digits=10, decimal_places=2)
    ddr4_compatibility = models.BooleanField(default=False)
    ddr5_compatibility = models.BooleanField(default=False)
    socket_type = models.CharField(max_length=255)
    wattage_compatibility = models.DecimalField(max_digits=10, decimal_places=2)
    bios_compatibility = models.BooleanField(default=False)
    chipset_compatibility = models.BooleanField(default=False)

    def check_compatibility(self, part_list):
        pass

    def __str__(self):
        return (
                super().__str__()
                + f"\nArchitecture: {self.architecture}\nClock Speed: {self.clock_speed}\n"
        )