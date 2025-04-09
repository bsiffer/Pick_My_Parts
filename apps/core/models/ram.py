from django.db import models
from apps.core.models.part import Part
from apps.core.models.motherboard import Motherboard 

class RAM(Part, models.Model):
    capacity_in_gb = models.IntegerField()
    ddr_standard = models.CharField(max_length=255)
    speed_in_mhz = models.IntegerField()
    sticks = models.IntegerField()
    latency = models.CharField(max_length=255)
    rgb = models.BooleanField()
    color = models.CharField(max_length=255)

    def check_compatibility(self, parts_list):
        incompatibilities = []

    # Check if the motherboard is selected
        motherboard_parts = parts_list.parts.get("Motherboard", [])
        if motherboard_parts:
            for motherboard in motherboard_parts:
                if self.ddr_standard != motherboard.supported_ram_type:
                    incompatibilities.append(
                        f"{self.get_name()} is incompatible: RAM type {self.ddr_standard} does not match motherboard's supported type {motherboard.supported_ram_type}."
                    )
            # Example check for number of RAM slots
                elif self.sticks > motherboard.ram_slots:
                    incompatibilities.append(
                        f"{self.get_name()} is incompatible: The motherboard only supports {motherboard.ram_slots} RAM slots, but {self.sticks} sticks were selected."
                    )

        return incompatibilities

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
