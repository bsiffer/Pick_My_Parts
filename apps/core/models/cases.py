from part import Part

class ComputerCase(Part):
    """Represents a computer case with attributes related to size, color, and compatibility."""

    def __init__(self, manufacturer, name, sku, price, form_factor, color, supported_form_factors):
        """Initializes a ComputerCase instance."""
        super().__init__(manufacturer, name, sku, price)
        self.__form_factor = form_factor
        self.__color = color
        self.__supported_form_factors = supported_form_factors  # List of supported motherboard form factors

    def get_form_factor(self):
        return self.__form_factor

    def set_form_factor(self, form_factor):
        self.__form_factor = form_factor

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_supported_form_factors(self):
        return self.__supported_form_factors

    def add_supported_form_factor(self, form_factor):
        """Adds a motherboard form factor if not already present."""
        if form_factor not in self.__supported_form_factors:
            self.__supported_form_factors.append(form_factor)

    def remove_supported_form_factor(self, form_factor):
        """Removes a motherboard form factor if present."""
        if form_factor in self.__supported_form_factors:
            self.__supported_form_factors.remove(form_factor)

    def check_compatibility(self, parts_list):
        """Checks if the case can accommodate the selected motherboard."""
        issues = []

        motherboard = parts_list.get_part("Motherboard")
        if motherboard:
            if motherboard.get_form_factor() not in self.__supported_form_factors:
                issues.append(
                    f"Case does not support the motherboard's form factor ({motherboard.get_form_factor()})."
                )

        return issues

    def to_string(self):
        """Returns a string representation of the computer case."""
        base_info = super().to_string()
        return (f"{base_info}\nForm Factor: {self.__form_factor}, Color: {self.__color}, "
                f"Supported Motherboard Sizes: {', '.join(self.__supported_form_factors)}")
