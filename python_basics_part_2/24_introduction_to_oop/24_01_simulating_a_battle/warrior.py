# Warrior Class Definition
# This script defines the Warrior class used in a simulated battle.

class Warrior:
    """ Represents a warrior in the battle. """

    def __init__(self, name: str) -> None:
        """
        Initializes a new Warrior instance.

        Args:
            name (str): The name of the warrior.
        """
        self.name = name
        self.health = 100

    def attack(self, opponent: 'Warrior') -> None:
        """
        Attacks another warrior, causing a decrease in their health.

        Args:
            opponent (Warrior): The warrior to be attacked.
        """
        damage = 20
        print(f"{self.name} attacks {opponent.name}! {opponent.name} loses {damage} health points.")
        opponent.health -= damage
        print(f"{opponent.name} has {opponent.health} health points remaining.\n")
