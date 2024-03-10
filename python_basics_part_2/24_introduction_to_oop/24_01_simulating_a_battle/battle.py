# Battle Class Definition
# This script defines the Battle class to manage a fight between two warriors.

import random

from warrior import Warrior  # Importing Warrior class


class Battle:
    """ Manages a battle between two warriors. """

    def __init__(self, warrior1: Warrior, warrior2: Warrior) -> None:
        """
        Initializes a new Battle instance.

        Args:
            warrior1 (Warrior): The first warrior participating in the battle.
            warrior2 (Warrior): The second warrior participating in the battle.
        """
        self.warrior1 = warrior1
        self.warrior2 = warrior2

    def start_battle(self) -> None:
        """
        Starts the battle between the warriors and continues until one loses all health.
        """
        print(f"The battle begins between {self.warrior1.name} and {self.warrior2.name}!\n")

        while self.warrior1.health > 0 and self.warrior2.health > 0:
            attacker, opponent = random.sample([self.warrior1, self.warrior2], 2)
            attacker.attack(opponent)

        self._print_winner()

    def _print_winner(self) -> None:
        """ Prints the winner of the battle. """
        if self.warrior1.health <= 0:
            print(f"{self.warrior2.name} emerges victorious!")
        else:
            print(f"{self.warrior1.name} emerges victorious!")
