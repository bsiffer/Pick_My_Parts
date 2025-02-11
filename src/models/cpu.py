# CPU class inheriting from part.py
from part import Part


class cpu(Part):
    # Constructor to create a CPU.
    def __init__(
        self,
        manufacturer: str,
        name: str,
        sku: int,
        price: float,
        architecture: str,
        clock_speed: float,
        # Compatibility to be determined later
    ):
        # Call super class constructor
        super().__init__(manufacturer, name, sku, price)
        self.__architecture = architecture
        self.__clock_speed = clock_speed

    # Getters and Setters for private variables __architecture and __clock_speed
    def get_architecture(self):
        return self.__architecture

    def get_clock_speed(self):
        return self.__clock_speed

    def set_architecture(self, architecture):
        self.__architecture = architecture

    def set_clock_speed(self, clock_speed):
        self.__clock_speed = clock_speed

    # Method to display part and CPU details.
    def display_info(self):
        return (
            super().display_info()
            + f"Architecture: {self.__architecture}\nClock Speed: {self.__clock_speed}\n"
        )
