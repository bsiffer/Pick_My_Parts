from django.db import models
from apps.core.models.part import Part

class Motherboard(Part, models.Model):
    socket_type = models.CharField(max_length=255)
    form_factor = models.CharField(max_length=255)
    ram_slots = models.IntegerField()
    supported_ram_type = models.CharField(max_length=255)
    chipset_compatibility = models.CharField(max_length=255)
    bios_compatibility = models.CharField(max_length=255)
    
    def check_compatibility(self, parts_list):
        pass

    def __str__(self):
        """Returns a string representation of the motherboard."""
        base_info = super().__str__()
        return (
            f"{base_info}\nSocket Type: {self.socket_type}, Form Factor: {self.form_factor}, "
            f"RAM Slots: {self.ram_slots}, Supported RAM Type: {self.supported_ram_type}"
        )