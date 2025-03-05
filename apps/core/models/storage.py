from apps.core.models.part import Part

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

    def to_string(self):
        """
        Returns storage details.
        """
        base_info = super().to_string()
        return (f"{base_info}\nType: {self.storage_type}, Size: {self.size}GB, "
                f"Compatibility: {self.compatibility}")