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
        issues = []
        motherboard = part_list.parts["Motherboard"]
        power_supply = part_list.parts["PowerSupply"]
        ram = part_list.parts["RAM"]

        if motherboard != []:  # Check if a motherboard is in the part list.
            if not self.socket_type == part_list["motherboard"].get_socket_type():
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Motherboard {part_list['motherboard'].get_name()}"
                )
            if (
                not self.bios_compatibility
                == part_list["motherboard"].get_bios_compatibility()
            ):
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Motherboard {part_list['motherboard'].get_name()}"
                )
            if (
                not self.chipset_compatibility
                == part_list["motherboard"].get_chipset_compatibility()
            ):
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Motherboard {part_list['motherboard'].get_name()}"
                )
        else:
            issues.append("no motherboard selected")

        if power_supply != []:
            if (
                not self.wattage_compatibility
                <= part_list["power_supply"].get_wattage()
            ):
                issues.append(
                    f"CPU {self.get_name()} is not compatible with Power Supply {part_list['power_supply'].get_name()}"
                )
        else:
            issues.append("no power supply selected")

        if ram != []:  # Check if a RAM stick/sticks are in the part list.
            for ram in part_list["ram"]:
                if (
                    not self.ddr4_compatibility
                    and ram.get_ddr_standard() == "DDR4"
                    or not self.ddr5_compatibility
                    and ram.get_ddr_standard() == "DDR5"
                ):
                    issues.append(
                        f"CPU {self.get_name()} is not compatible with RAM {ram.get_name()}"
                    )
        else:
            issues.append("no ram selected")
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
