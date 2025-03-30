from django.db import models
from apps.core.models.form_factor import FormFactor
from apps.core.models.part import Part

class ComputerCase(Part, models.Model):
    """Represents a computer case with attributes related to size, color, and compatibility."""
    form_factor = models.ForeignKey(FormFactor, on_delete=models.SET_NULL, null=True, related_name="primary_cases")
    color = models.CharField(max_length=255)
    supported_form_factors = models.ManyToManyField(FormFactor, related_name="compatible_cases")

    def check_compatibility(self, parts_list):
        """Checks if the case can accommodate the selected motherboard."""
        pass

    def __str__(self):
        """Returns a string representation of the computer case."""
        base_info = super().__str__()
        return (
            f"{base_info}\nForm Factor: {self.form_factor},"
            f"\nColor: {self.color},"
            f"\nSupported Form Factors: {self.supported_form_factors}"
        )