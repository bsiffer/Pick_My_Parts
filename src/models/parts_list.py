from src.models.part import Part

class PartsList:
    """
    Represents a list of parts selected by the user.
    Provides methods to create, read, update, and delete parts in the list.
    """
    
    def __init__(self):
        # initializes an empty dictionary to store parts by SKU, allowing multiple instances per SKU
        self.parts = {}
        self.incompatibilities = []
    
    def add_part(self, part: Part):
        """Adds a part to the dictionary, allowing multiple parts with the same SKU."""
        
        if part.get_sku() in self.parts:
            self.parts[part.get_sku()].append(part)  # append to existing list
        else:
            self.parts[part.get_sku()] = [part]  # create new list

        print(f"Part added: {part.get_name()} ({part.get_sku()})")

        # check compatibility after adding a new part
        self.check_compatibility()
    
    def remove_part(self, sku: int):
        """Removes one instance of a part with the given SKU, or all if only one exists."""
        
        if sku in self.parts:
            if len(self.parts[sku]) > 1:
                removed_part = self.parts[sku].pop(0)  # remove one instance
            else:
                removed_part = self.parts.pop(sku)[0]  # remove last instance
            
            print(f"Removed: {removed_part.get_name()} ({removed_part.get_sku()})")

            # re-check compatibility after removal
            self.check_compatibility()
        else:
            print(f"No part with SKU {sku} found.")
    
    def update_part(self, sku: int, attribute: str, new_value):
        """Updates an attribute of a part in the dictionary by SKU."""
        
        if sku in self.parts:
            for part in self.parts[sku]:  # update all instances of the SKU
                if hasattr(part, attribute):
                    setattr(part, attribute, new_value)
                    print(f"Updated {attribute} of {part.get_name()} to {new_value}")
                else:
                    print(f"Attribute '{attribute}' not found in {part.get_name()}")
        else:
            print(f"No part with SKU {sku} found.")
    
    def get_part(self, sku: int):
        """Returns all parts with a given SKU, or None if not found."""
        return self.parts.get(sku, None)
    
    def display_parts(self):
        """Displays all parts in the dictionary."""
        
        if not self.parts:
            print("No parts in the list.")
            return
        for part_list in self.parts.values():
            for part in part_list:
                print(part.display_info())
    
    def check_compatibility(self):
        """Runs compatibility checks for all parts in the dictionary."""
        
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
    
    def clear_list(self):
        """Clears all parts from the dictionary."""
        
        self.parts.clear()
        self.incompatibilities = []
        print("Parts list cleared.")
