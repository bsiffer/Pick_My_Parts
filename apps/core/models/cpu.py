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
                + f"\nArchitecture: {self.architecture}"
                  f"\nClock Speed: {self.clock_speed}"
                  f"\nDDR4 Compatibility = {self.ddr4_compatibility}"
                  f"\nDDR5 Compatibility = {self.ddr5_compatibility}"
                  f"\nSocket Type = {self.socket_type}"
                  f"\nWattage Compatibility = {self.wattage_compatibility}"
                  f"\nBIOS Compatibility = {self.bios_compatibility}"
                  f"\nChipset Compatibility = {self.chipset_compatibility}"
        )