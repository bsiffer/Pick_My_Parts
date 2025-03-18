from apps.core.models.part import Part


class PartsList:
    """Represents a list of parts selected by the user."""

    def __init__(self):
        """Initializes a dictionary with predefined part types set to None."""
        self.parts = {
            "Case": [],
            "CPU": [],
            "GPU": [],
            "Motherboard": [],
            "PowerSupply": [],
            "RAM": [],
        }
        self.incompatibilities = []

    def add_part(self, part: Part):
        """Adds a new part to the dictionary and checks compatibility."""
        part_type = part.get_part_type()
        if part_type not in self.parts:
            print(f"Invalid part type: {part_type}")
            return

        self.parts[part_type].append(part)
        print(f"Part added: {part.get_name()} ({part.get_sku()})")

        # Check compatibility after adding a new part
        self.check_compatibility()

    def remove_part(self, sku: int):
        """Removes a part from the dictionary by SKU."""
        for part_type, part_list in self.parts.items():
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
                    setter_method = f"set_{attribute[1:]}"
                    if hasattr(part, setter_method):
                        getattr(part, setter_method)(new_value)
                        print(
                            f"Updated {attribute} of {part.get_name()} to {new_value}"
                        )
                    else:
                        print(
                            f"Attribute '{attribute}' cannot be updated in {part.get_name()}."
                        )
                    return
        print(f"No part with SKU {sku} found.")

    def display_parts(self):
        """Displays all parts in the dictionary."""
        if not any(self.parts.values()):
            print("No parts in the list.")
            return
        for part_type, part_list in self.parts.items():
            if not part_list:
                print(f"part_type: None")
            else:
                for part in part_list:  # Handles None or empty lists
                    print(part.display_info())  # Calls __str__()

    def check_compatibility(self):
        """Checks compatibility of all parts in the list."""
        self.incompatibilities = []

        for part_list in self.parts.values():
            if part_list:
                for part in part_list:
                    if hasattr(part, "check_compatibility") and callable(
                        part.check_compatibility
                    ):
                        issues = part.check_compatibility(self)
                        if issues:
                            self.incompatibilities.extend(issues)

        if self.incompatibilities:
            print("Compatibility issues found:")
            for issue in self.incompatibilities:
                print(issue)
        else:
            print("All parts are compatible.")

    def clear_list(self):
        """Resets all parts to None and cleard incompatibilities."""
        for part_type in self.parts.keys():
            self.parts[part_type] = []
        self.incompatibilities = []
        print("Parts list cleared.")
