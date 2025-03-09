class Part:
    """Represents a generic part with manufacturer, name, SKU, and price attributes."""

    def __init__(self, manufacturer, name, sku, price):
        """Initializes a Part instance."""
        self.__manufacturer = manufacturer
        self.__name = name
        self.__sku = sku
        self.set_price(price)  # Use setter to ensure validation

    def get_manufacturer(self):
        return self.__manufacturer

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_sku(self):
        return self.__sku

    def set_sku(self, sku):
        self.__sku = sku

    def get_price(self):
        return self.__price

    def set_price(self, price):
        """Ensures price is not negative before setting it."""
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = price

    def __str__(self):
        """Returns a string representation of the part."""
        return (f"Manufacturer: {self.__manufacturer}\n"
                f"Name: {self.__name}\n"
                f"SKU: {self.__sku}\n"
                f"Price: ${self.__price:.2f}")
