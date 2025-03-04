from part import Part


class PartsList:
    """
    Represents a list of parts selected by the user.
    Provides methods to create, read, update, and delete parts in the list.
    """

    # initializes an empty list to store parts
    def __init__(self):
        self.parts = []
        self.incompatibilities = []

    # adds a new part to the list
    def add_part(self, part: Part):
        self.parts.append(part)
        print(f"Part added: {part.get_name()} ({part.get_sku()})")

    # removes a part from the list by SKU
    def remove_part(self, sku: int):
        for part in self.parts:
            if part.get_sku() == sku:
                self.parts.remove(part)
                print(f"Part removed: {part.get_name()} ({part.get_sku()})")
                return
        print("Part not found.")

    # updates an attribute of a part in the list by SKU
    def update_part(self, sku: int, attribute: str, new_value):
        for part in self.parts:
            if part.get_sku() == sku:
                if hasattr(part, attribute):
                    setattr(part, attribute, new_value)
                    print(f"Updated {attribute} of {part.get_name()} to {new_value}")
                else:
                    print(f"Attribute '{attribute}' not found in {part.get_name()}")
                return
        print("Part not found.")

    # retrieves a part from the list by SKU
    def get_part(self, sku: int):
        for part in self.parts:
            if part.get_sku() == sku:
                return part
        print("Part not found.")
        return None

    # displays all parts in the list
    def display_parts(self):
        if not self.parts:
            print("No parts in the list.")
            return
        for part in self.parts:
            print(part.display_info())

    # clears all parts from the list
    def clear_list(self):
        self.parts.clear()
        print("Parts list cleared.")

    # placeholder for compatibility checking
    def check_compatibility(self):
        self.incompatibilities = []
        for part in self.parts:
            if hasattr(part, "check_compatibility") and callable(
                part.check_compatibility
            ):
                issues = part.check_compatibility(self.parts)
                if issues:
                    self.incompatibilities.extend(issues)
            if self.incompatibilities:
                print("Compatibility issues: ")
                for issue in self.incompatibilities:
                    print(issue)
            else:
                print("All parts are compatible.")
