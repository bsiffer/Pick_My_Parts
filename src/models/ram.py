from ..models.part import Part


class Ram(Part):
    def __init__(self, manufacturer: str, name: str, sku: int, price: float, capacity: int,
                 standard: str, speed: int, sticks: int, latency: int, rgb: bool, color: str) -> None:

        super().__init__(manufacturer, name, sku, price)
        self.__capacity = capacity  # Defines the storage capacity of the kit in GB
        self.__ddr_standard = standard  # Defines the DDR standard of the kit
        self.__speed = speed  # Defines the rated speed of the kit
        self.__sticks = sticks  # Defines the amount of ram sticks in the kit
        self.__latency = latency  # Defines the CAS latency of the kit
        self.__rgb = rgb  # Defines if the kit has RGB effects or not
        self.__color = color  # Defines the primary color of the kit

    # Get and set methods for RAM class
    def get_capacity(self) -> int:
        return self.__capacity

    def set_capacity(self, capacity: int) -> None:
        self.__capacity = capacity

    def get_ddr_standard(self) -> str:
        return self.__ddr_standard

    def set_ddr_standard(self, ddr_standard: str) -> None:
        self.__ddr_standard = ddr_standard

    def get_speed(self) -> int:
        return self.__speed

    def set_speed(self, speed: int) -> None:
        self.__speed = speed

    def get_sticks(self) -> int:
        return self.__sticks

    def set_sticks(self, sticks: int) -> None:
        self.__sticks = sticks

    def get_latency(self) -> int:
        return self.__latency

    def set_latency(self, latency: int) -> None:
        self.__latency = latency

    def get_rgb(self) -> bool:
        return self.__rgb

    def set_rgb(self, rgb: bool) -> None:
        self.__rgb = rgb

    def get_color(self) -> str:
        return self.__color

    def set_color(self, color: str) -> None:
        self.__color = color

    # Information display for the RAM class
    def display_info(self):
        part_information = super().display_info()
        print(f'{part_information}\n'
              f'Part Name: {self.__name}\n'
              f'Price: {self.__price}\n'
              f'SKU: {self.__sku}\n'
              f'Manufacturer: {self.__manufacturer}\n'
              f'Capacity: {self.__capacity}\n'
              f'DDR Standard: {self.__ddr_standard}\n'
              f'Speed: {self.__speed}\n'
              f'Sticks: {self.__sticks}\n '
              f'CAS Latency: {self.__latency}\n'
              f'RGB: {self.__rgb}\n'
              f'Color: {self.__color}')
