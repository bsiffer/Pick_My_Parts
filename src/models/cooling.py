from src.models.part import Part


class CoolingAccessory(Part):
    """
    Class that represents Cooling Accessory

    Attributes
    ----------
    __cooling_type : str
        Cooling Accessory Type (Air/Liquid)
    """
    def __init__(self, manufacturer: str, name: str, sku: int, price: float, cooling_type: str) -> None:
        """
        Constructor for CoolingAccessory class.
        :param manufacturer: Cooling Accessory Manufacturer
        :param name: Cooling Accessory Name
        :param sku: Cooling Accessory SKU
        :param price: Cooling Accessory Price
        :param cooling_type: Cooling Accessory Type (Air/Liquid)
        """
        super().__init__(manufacturer, name, sku, price)
        self.__cooling_type = cooling_type

    def get_cooling_type(self) -> str:
        """
        Getter for Private variable __cooling_type
        :return: __cooling_type
        """
        return self.__cooling_type

