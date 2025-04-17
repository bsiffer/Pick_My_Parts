from django.db import models

class Part(models.Model):
    """Represents a generic part with manufacturer, name, SKU, and price attributes."""

    manufacturer = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sku = models.IntegerField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_price(self):
        """Returns the price of the part."""
        return self.price

    def get_sku(self):
        """Returns the SKU of the part."""
        return self.sku
    
    def get_name(self):
        """Returns the name of the part."""
        return self.name
    
    def get_part_type(self):
        """Returns the type of the part."""
        return self.__class__.__name__

    def set_price(self, price):
        """Ensures price is not negative before setting it."""
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = price

    def __str__(self):
        """Returns a string representation of the part."""
        return (f"Manufacturer: {self.manufacturer}\n"
                f"Name: {self.name}\n"
                f"SKU: {self.sku}\n"
                f"Price: ${self.price:.2f}")

    class Meta:
        abstract = True
        app_label = 'core'