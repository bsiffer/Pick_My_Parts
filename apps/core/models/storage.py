from part import Part


class Storage(Part):
    """Represents a storage device with attributes related to type, capacity, and compatibility."""

    def __init__(
        self, manufacturer, name, sku, price, storage_type, capacity, interface
    ):
        """Initializes a Storage instance."""
        super().__init__(manufacturer, name, sku, price)
        self.__storage_type = storage_type  # e.g., HDD, SSD, NVMe
        self.__capacity = capacity  # Storage size in GB
        self.__interface = interface  # e.g., SATA, PCIe

    def get_storage_type(self):
        return self.__storage_type

    def set_storage_type(self, storage_type):
        self.__storage_type = storage_type

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_interface(self):
        return self.__interface

    def set_interface(self, interface):
        self.__interface = interface

    def check_compatibility(self, parts_list):
        """Checks if the storage device is compatible with the selected motherboard."""
        issues = []
        motherboard = parts_list.parts["Motherboard"]

        if motherboard != []:
            if self.__interface not in motherboard.get_supported_storage_interfaces():
                issues.append(
                    f"Motherboard does not support {self.__interface} storage interface."
                )
        else:
            issues.append("No motherboard selected.")

        return issues

    def to_string(self):
        """Returns a string representation of the storage device."""
        base_info = super().to_string()
        return (
            f"{base_info}\nType: {self.__storage_type}\n"
            f"Capacity: {self.__capacity}GB\n"
            f"Interface: {self.__interface}"
        )
