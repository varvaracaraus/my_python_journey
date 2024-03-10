class House:
    """Represents a house with food and money."""

    def __init__(self):
        """
        Initialize a new house with default food and money.
        """
        self.food = 50
        self.money = 0

    def add_food(self, amount: int) -> None:
        """Add a specified amount of food to the house."""
        self.food += amount

    def remove_food(self, amount: int) -> None:
        """Remove a specified amount of food from the house."""
        self.food -= amount

    def add_money(self, amount: int) -> None:
        """Add a specified amount of money to the house."""
        self.money += amount

    def remove_money(self, amount: int) -> None:
        """Remove a specified amount of money from the house."""
        self.money -= amount
