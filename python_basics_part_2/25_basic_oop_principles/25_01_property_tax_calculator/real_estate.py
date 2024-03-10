from property import Property


class Apartment(Property):
    """
    Represents an apartment property.
    """

    def tax(self) -> float:
        """
        Calculate the tax for the apartment.

        Returns:
            float: The tax for the apartment.
        """
        return self.get_worth() / 1000


class Car(Property):
    """
    Represents a car property.
    """

    def tax(self) -> float:
        """
        Calculate the tax for the car.

        Returns:
            float: The tax for the car.
        """
        return self.get_worth() / 200


class CountryHouse(Property):
    """
    Represents a country house property.
    """

    def tax(self) -> float:
        """
        Calculate the tax for the country house.

        Returns:
            float: The tax for the country house.
        """
        return self.get_worth() / 500
