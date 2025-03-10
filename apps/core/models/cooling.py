from part import Part

class CoolingAccessory(Part):
    """Represents a cooling accessory with attributes related to cooling type and compatibility."""

    def __init__(self, manufacturer, name, sku, price, cooling_type):
        """Initializes a CoolingAccessory instance."""
        super().__init__(manufacturer, name, sku, price)
        self.__cooling_type = cooling_type  # e.g., Air or Liquid

    def get_cooling_type(self):
        return self.__cooling_type

    def set_cooling_type(self, cooling_type):
        self.__cooling_type = cooling_type

    def check_compatibility(self, parts_list):
        """Checks if the cooling accessory is compatible with the selected CPU."""
        issues = []

        cpu = parts_list.get_part("CPU")
        if cpu:
            if cpu.get_supported_cooling_type() and self.__cooling_type not in cpu.get_supported_cooling_type():
                issues.append(
                    f"Cooling type {self.__cooling_type} is not supported by the selected CPU."
                )

        return issues

    def to_string(self):
        """Returns a string representation of the cooling accessory."""
        base_info = super().to_string()
        return f"{base_info}\nCooling Type: {self.__cooling_type}"
