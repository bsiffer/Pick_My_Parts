from django.db import models
from apps.core.models.part import Part

class CPU(Part, models.Model):
    architecture = models.CharField(max_length=255)
    clock_speed = models.DecimalField(max_digits=10, decimal_places=2)
    ddr4_compatibility = models.BooleanField(default=False)
    ddr5_compatibility = models.BooleanField(default=False)
    socket_type = models.CharField(max_length=255)
    wattage_compatibility = models.DecimalField(max_digits=10, decimal_places=2)
    bios_compatibility = models.CharField(max_length=255)
    chipset_compatibility = models.CharField(max_length=255)

    def check_compatibility(self, part_list):
        issues = []
        motherboards = part_list.parts.get("Motherboard", [])
        power_supplies = part_list.parts.get("PowerSupply", [])
        ram_modules = part_list.parts.get("RAM", [])

        if len(motherboards) == 1:
            # Assume only one motherboard can be selected.
            motherboard = motherboards[0]
            if self.socket_type != motherboard.socket_type:
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Motherboard {motherboard.get_name()} (Socket mismatch)."
                )
            if self.bios_compatibility != motherboard.bios_compatibility:
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Motherboard {motherboard.get_name()} (BIOS mismatch)."
                )
            if self.chipset_compatibility != motherboard.chipset_compatibility:
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Motherboard {motherboard.get_name()} (Chipset mismatch)."
                )

        for power_supply in power_supplies:
            if self.wattage_compatibility > power_supply.rated_wattage:
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Power Supply {power_supply.get_name()}"
                )

        for ram in ram_modules:
            if not (self.ddr4_compatibility and ram.ddr_standard == "DDR4") and not (self.ddr5_compatibility and ram.ddr_standard == "DDR5"):
                issues.append(
                    f"CPU {self.get_name()} is not compatible with RAM {ram.get_name()}"
                )

        return issues

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
