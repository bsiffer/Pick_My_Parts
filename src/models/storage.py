from src.models.part import Part

class Storage(Part):
    """
    Represents a storage device.
    """
    def __init__(self, manufacturer, part_name, sku, price, storage_type, size, compatibility):
        """
        Initializes Storage with attributes.
        """
        super().__init__(manufacturer, part_name, sku, price)
        self.storage_type = storage_type
        self.size = size
        self.compatibility = compatibility

    def display_info(self):
        """
        Returns storage details.
        """
        base_info = super().display_info()
        return (f"{base_info}\nType: {self.storage_type}, Size: {self.size}GB, "
                f"Compatibility: {self.compatibility}")