from part import Part

class ComputerCase(Part):
    """Represents a computer case with attributes related to size, color, and compatibility."""

    def __init__(self, manufacturer, name, sku, price, form_factor, color, supported_form_factors, 
                 max_gpu_length, max_cpu_cooler_height, supported_psu_form_factors, max_psu_length):
        """Initializes a ComputerCase instance."""
        super().__init__(manufacturer, name, sku, price)
        self.__form_factor = form_factor
        self.__color = color
        self.__supported_form_factors = supported_form_factors  # List of supported motherboard form factors
        self.__max_gpu_length = max_gpu_length  # Maximum GPU length in mm
        self.__max_cpu_cooler_height = max_cpu_cooler_height  # Max CPU cooler height in mm
        self.__supported_psu_form_factors = supported_psu_form_factors  # List of supported PSU form factors
        self.__max_psu_length = max_psu_length  # Maximum PSU length in mm

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

    def get_max_gpu_length(self):
        return self.__max_gpu_length

    def get_max_cpu_cooler_height(self):
        return self.__max_cpu_cooler_height

    def get_supported_psu_form_factors(self):
        return self.__supported_psu_form_factors

    def get_max_psu_length(self):
        return self.__max_psu_length

    def add_supported_form_factor(self, form_factor):
        """Adds a motherboard form factor if not already present."""
        if form_factor not in self.__supported_form_factors:
            self.__supported_form_factors.append(form_factor)

    def remove_supported_form_factor(self, form_factor):
        """Removes a motherboard form factor if present."""
        if form_factor in self.__supported_form_factors:
            self.__supported_form_factors.remove(form_factor)

    def check_compatibility(self, parts_list):
        """Checks if the case can accommodate the selected motherboard, GPU, CPU cooler, and PSU."""
        issues = []

        # Motherboard Compatibility
        motherboard = parts_list.get_part("Motherboard")
        if motherboard:
            if motherboard.get_form_factor() not in self.__supported_form_factors:
                issues.append(
                    f"Case does not support the motherboard's form factor ({motherboard.get_form_factor()})."
                )

        # GPU Length Compatibility
        gpu = parts_list.get_part("GPU")
        if gpu:
            if gpu.get_length() > self.__max_gpu_length:
                issues.append(
                    f"GPU length ({gpu.get_length()}mm) exceeds the case's maximum supported length ({self.__max_gpu_length}mm)."
                )
            if gpu.get_slot_size() > self.get_slot_capacity():
                issues.append(
                    f"GPU requires {gpu.get_slot_size()} expansion slots, but case only supports {self.get_slot_capacity()}."
                )

        # CPU Cooler Height Compatibility
        cpu_cooler = parts_list.get_part("CPU Cooler")
        if cpu_cooler:
            if cpu_cooler.get_height() > self.__max_cpu_cooler_height:
                issues.append(
                    f"CPU cooler height ({cpu_cooler.get_height()}mm) exceeds the case's maximum supported height ({self.__max_cpu_cooler_height}mm)."
                )

        # Power Supply Compatibility
        psu = parts_list.get_part("PowerSupply")
        if psu:
            if psu.get_form_factor() not in self.__supported_psu_form_factors:
                issues.append(
                    f"Case does not support the power supply form factor ({psu.get_form_factor()})."
                )
            if psu.get_length() > self.__max_psu_length:
                issues.append(
                    f"Power supply length ({psu.get_length()}mm) exceeds the case's maximum supported length ({self.__max_psu_length}mm)."
                )

        return issues

    def to_string(self):
        """Returns a string representation of the computer case."""
        base_info = super().to_string()
        return (f"{base_info}\nForm Factor: {self.__form_factor}, Color: {self.__color}, "
                f"Supported Motherboard Sizes: {', '.join(self.__supported_form_factors)}\n"
                f"Max GPU Length: {self.__max_gpu_length}mm, Max CPU Cooler Height: {self.__max_cpu_cooler_height}mm\n"
                f"Supported PSU Form Factors: {', '.join(self.__supported_psu_form_factors)}, Max PSU Length: {self.__max_psu_length}mm")
