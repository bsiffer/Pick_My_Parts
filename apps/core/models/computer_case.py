from django.db import models
from apps.core.models.form_factor import FormFactor
from apps.core.models.part import Part

class ComputerCase(Part, models.Model):
    """Represents a computer case with attributes related to size, color, and compatibility."""
    form_factor = models.ForeignKey(FormFactor, on_delete=models.SET_NULL, null=True, related_name="primary_cases")
    color = models.CharField(max_length=255)
    supported_form_factors = models.ManyToManyField(FormFactor, related_name="compatible_cases")
    supported_cooling_types = models.JSONField(default=list)

    def check_compatibility(self, parts_list):
        issues = []
        motherboards = parts_list.parts.get("Motherboard", [])
        if len(motherboards) == 1:
            # Assume only one motherboard is selected.
            mb = motherboards[0]
            # Get the names of the supported form factors.
            supported = [ff.name for ff in self.supported_form_factors.all()]
            if mb.form_factor not in supported:
                issues.append(
                    f"Computer Case '{self.get_name()}' does not support the motherboard form factor '{mb.form_factor}'."
                )
        return issues

    def __str__(self):
        """Returns a string representation of the computer case."""
        base_info = super().__str__()
        return (
            f"{base_info}\nForm Factor: {self.form_factor},"
            f"\nColor: {self.color},"
            f"\nSupported Form Factors: {self.supported_form_factors}"
        )