from django.db import models
from apps.core.models.part import Part

class Motherboard(Part, models.Model):
    socket_type = models.CharField(max_length=255)
    form_factor = models.CharField(max_length=255)
    ram_slots = models.IntegerField()
    supported_ram_type = models.CharField(max_length=255)
    chipset_compatibility = models.CharField(max_length=255)
    bios_compatibility = models.CharField(max_length=255)
    supported_storage_interfaces = models.JSONField(default=list)
    
    def check_compatibility(self, parts_list):
        issues = []

        cpu = parts_list.parts.get("CPU")
        ram_modules = parts_list.parts.get("RAM", [])
        case = parts_list.parts.get("ComputerCase")
        storage_devices = parts_list.parts.get("Storage", [])

        # Check CPU compatibility
        if cpu:
            if cpu.socket_type != self.socket_type:
                issues.append(f"CPU socket type '{cpu.socket_type}' is not compatible with motherboard socket '{self.socket_type}'.")
            if cpu.bios_compatibility != bool(self.bios_compatibility):
                issues.append("CPU BIOS compatibility does not match the motherboard.")
            if cpu.chipset_compatibility != bool(self.chipset_compatibility):
                issues.append("CPU chipset compatibility does not match the motherboard.")
        else:
            issues.append("No CPU selected.")

        # Check RAM compatibility
        if ram_modules:
            if len(ram_modules) > self.ram_slots:
                issues.append(f"Too many RAM sticks selected. Motherboard supports only {self.ram_slots} slot(s).")
            for ram in ram_modules:
                if ram.ddr_standard != self.supported_ram_type:
                    issues.append(f"RAM {ram.get_name()} with DDR {ram.ddr_standard} is not compatible with motherboard DDR {self.supported_ram_type}.")
        else:
            issues.append("No RAM selected.")

        # Check Computer Case compatibility
        if case:
            if not case.supported_form_factors.filter(name=self.form_factor).exists():
                issues.append(f"Motherboard form factor '{self.form_factor}' is not supported by the selected case.")
        else:
            issues.append("No computer case selected.")

        # Check Storage compatibility
        if storage_devices:
            for storage in storage_devices:
                if storage.interface not in self.supported_storage_interfaces:
                    issues.append(f"Storage interface '{storage.interface}' not supported by the motherboard.")
        else:
            issues.append("No storage selected.")

        return issues

    def __str__(self):
        """Returns a string representation of the motherboard."""
        base_info = super().__str__()
        return (
            f"{base_info}\nSocket Type: {self.socket_type}, Form Factor: {self.form_factor}, "
            f"RAM Slots: {self.ram_slots}, Supported RAM Type: {self.supported_ram_type}"
        )