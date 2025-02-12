class ComputerCase:
    def __init__(self, name: str, size: str, color: str, compatibility: list):
        self.name = name
        self.size = size
        self.color = color
        self.compatibility = compatibility
    
    def is_compatible(self, motherboard_size: str) -> bool:
        return motherboard_size in self.compatibility
    
    def __str__(self):
        return f"{self.name} ({self.size}) - Color: {self.color}, Compatible with: {', '.join(self.compatibility)}"

# Example usage:
case1 = ComputerCase("NZXT H510", "ATX", "Black", ["ATX", "Micro-ATX", "Mini-ITX"])
print(case1)
print("Compatible with ATX:", case1.is_compatible("ATX"))
