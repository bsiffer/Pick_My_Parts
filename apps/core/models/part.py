class Part:
    """
    Class that represents the Part.

    Attributes
    ----------
    __manufacturer : str
        Private variable for the Part Manufacturer
    __name : str
        Private variable for the Part Name
    __sku : int
        Private variable for the Part SKU
    __price : float
        Private variable for the Part Price
    """
    def __init__(self, manufacturer: str, name: str, sku: int, price: float) -> None:
        """
        Constructor to create a Part.
        :param manufacturer: Part Manufacturer
        :param name: Part Name
        :param sku: Part SKU
        :param price: Part Price
        """
        self.__manufacturer = manufacturer
        self.__name = name
        self.__sku = sku
        self.__price = price

    def get_manufacturer(self) -> str:
        """
        Getter for private variable __manufacturer that represents Part Manufacturer
        :return: __manufacturer
        """
        return self.__manufacturer

    def get_name(self) -> str:
        """
        Getter for private variable __name that represents Part Name
        :return: __name
        """
        return self.__name

    def get_sku(self) -> int:
        """
        Getter for private variable __sku that represents Part SKU
        :return: __sku
        """
        return self.__sku

    def get_price(self) -> float:
        """
        Getter for private variable __price that represents Part Price
        :return: __price
        """
        return self.__price

    def set_manufacturer(self, manufacturer: str) -> None:
        """
        Setter for private variable __manufacturer
        :param manufacturer:
        """
        self.__manufacturer = manufacturer

    def set_name(self, name: str) -> None:
        """
        Setter for private variable __name
        :param name: Part Name
        """
        self.__name = name

    def set_sku(self, sku: int) -> None:
        """
        Setter for private variable __sku
        :param sku: Part SKU
        """
        self.__sku = sku

    def set_price(self, price: float) -> None:
        """
        Setter for private variable __price
        :param price: Part Price
        """
        self.__price = price

    def to_string(self) -> str:
        """
        Method to display Part's Information
        """
        return(f'Part Name: {self.__name}\nPrice: {self.__price}\n'
              f'SKU: {self.__sku}\nManufacturer: {self.__manufacturer}')
