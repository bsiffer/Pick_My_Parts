from src.models.part import Part

class ComputerCase(Part):
    def __init__(self, manufacturer: str, name: str, sku: int, price: float, size: str, color: str, compatibility: list):
        super().__init__(manufacturer, name, sku, price)
        self.size = size
        self.color = color
        self.compatibility = compatibility
    
    def is_compatible(self, motherboard_size: str) -> bool:
        return motherboard_size in self.compatibility
    
    def to_string(self):
        base_info = super().to_string()
        return f"{base_info}\nSize: {self.size}, Color: {self.color}, Compatible with: {', '.join(self.compatibility)}"

# Example usage:
case1 = ComputerCase("NZXT", "H510", 123456, 99.99, "ATX", "Black", ["ATX", "Micro-ATX", "Mini-ITX"])
print(case1.to_string())
print("Compatible with ATX:", case1.is_compatible("ATX"))
