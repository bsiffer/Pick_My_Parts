from part import Part

class PartsList:
    """Represents a list of parts selected by the user."""

    def __init__(self):
        """Initializes an empty dictionary to store parts."""
        self.parts = {}
        self.incompatibilities = []

    def add_part(self, part: Part):
        """Adds a new part to the dictionary and checks compatibility."""
        part_type = part.__class__.__name__
        if part_type not in self.parts:
            self.parts[part_type] = []
        self.parts[part_type].append(part)
        print(f"Part added: {part.get_name()} ({part.get_sku()})")

        # Check compatibility after adding a new part
        self.check_compatibility()

    def remove_part(self, sku: int):
        """Removes a part from the dictionary by SKU."""
        for part_type, part_list in list(self.parts.items()):
            for part in part_list:
                if part.get_sku() == sku:
                    part_list.remove(part)
                    print(f"Removed: {part.get_name()} ({part.get_sku()})")
                    self.check_compatibility()  # Checking remaining compatibility
                    return
        print(f"No part with SKU {sku} found.")

    def update_part(self, sku: int, attribute: str, new_value):
        """Updates an attribute of a part in the dictionary by SKU."""
        for part_list in self.parts.values():
            for part in part_list:
                if part.get_sku() == sku:
                    if hasattr(part, f"set_{attribute}"):
                        getattr(part, f"set_{attribute}")(new_value)
                        print(f"Updated {attribute} of {part.get_name()} to {new_value}")
                    else:
                        print(f"Attribute '{attribute}' cannot be updated in {part.get_name()}.")
                    return
        print(f"No part with SKU {sku} found.")

    def display_parts(self):
        """Displays all parts in the dictionary."""
        if not self.parts:
            print("No parts in the list.")
            return
        for part_list in self.parts.values():
            for part in part_list:
                print(part)  # Calls __str__()

    def check_compatibility(self):
        """Checks compatibility of all parts in the list."""
        self.incompatibilities = []
        for part_list in self.parts.values():
            for part in part_list:
                if hasattr(part, "check_compatibility") and callable(part.check_compatibility):
                    issues = part.check_compatibility(self)
                    if issues:
                        self.incompatibilities.extend(issues)

        if self.incompatibilities:
            print("Compatibility issues found:")
            for issue in self.incompatibilities:
                print(issue)
        else:
            print("All parts are compatible.")
