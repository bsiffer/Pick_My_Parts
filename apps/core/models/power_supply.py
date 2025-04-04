from part import Part


class PowerSupply(Part):
    """Represents a power supply unit (PSU) with attributes for size, wattage, efficiency, and compatibility."""

    def __init__(
        self,
        manufacturer,
        name,
        sku,
        price,
        size_standard,
        rated_wattage,
        certification_level,
        modular,
        efficiency_rating_percentage,
        pcie_connectors,
        length,
    ):
        """Initializes a PowerSupply instance."""
        super().__init__(manufacturer, name, sku, price)
        self.__size_standard = size_standard
        self.__rated_wattage = rated_wattage
        self.__certification_level = certification_level
        self.__modular = modular
        self.__efficiency_rating_percentage = efficiency_rating_percentage
        self.__pcie_connectors = pcie_connectors
        self.__length = length

    def get_size_standard(self):
        return self.__size_standard

    def set_size_standard(self, size_standard):
        self.__size_standard = size_standard

    def get_rated_wattage(self):
        return self.__rated_wattage

    def set_rated_wattage(self, rated_wattage):
        self.__rated_wattage = rated_wattage

    def get_certification_level(self):
        return self.__certification_level

    def set_certification_level(self, certification_level):
        self.__certification_level = certification_level

    def get_modular(self):
        return self.__modular

    def set_modular(self, modular):
        self.__modular = modular

    def get_efficiency_rating_percentage(self):
        return self.__efficiency_rating_percentage

    def set_efficiency_rating_percentage(self, efficiency_rating_percentage):
        self.__efficiency_rating_percentage = efficiency_rating_percentage

    def get_pcie_connectors(self):
        return self.__pcie_connectors

    def set_pcie_connectors(self, pcie_connectors):
        self.__pcie_connectors = pcie_connectors

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def check_compatibility(self, parts_list):
        """Checks PSU compatibility with GPU and power requirements."""
        issues = []
        gpu = parts_list.parts["GPU"]

        # Check GPU power requirements
        if gpu != []:
            if gpu.get_required_wattage() > self.__rated_wattage:
                issues.append(
                    f"GPU requires {gpu.get_required_wattage()}W, but PSU is only rated for {self.__rated_wattage}W."
                )

            if gpu.get_required_pcie_connectors() > self.__pcie_connectors:
                issues.append(
                    f"GPU requires {gpu.get_required_pcie_connectors()} PCIe connectors, but PSU only provides {self.__pcie_connectors}."
                )
        else:
            issues.append("No GPU selected.")

        return issues

    def to_string(self):
        """Returns a string representation of the power supply."""
        base_info = super().to_string()
        return (
            f"{base_info}\n"
            f"Size Standard: {self.__size_standard}\n"
            f"Wattage: {self.__rated_wattage}W\n"
            f"Certification: {self.__certification_level}\n"
            f"Modular: {self.__modular}\n"
            f"Efficiency Rating: {self.__efficiency_rating_percentage}%\n"
            f"PCIe Connectors: {self.__pcie_connectors}\n"
            f"Length: {self.__length}mm"
        )
