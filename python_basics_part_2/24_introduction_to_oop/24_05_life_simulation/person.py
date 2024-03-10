import random

from house import House


class Person:
    """Represents a person living in a house."""

    def __init__(self, name: str, house: House):
        """
        Initialize a new person.

        Args:
            name (str): The name of the person.
            house (House): The house where the person lives.
        """
        self.name = name
        self.satiety = 50  # Renamed from 'fullness' for clarity
        self.house = house

    def __str__(self):
        return f'{self.name} satiety level: {self.satiety}'

    def eat(self) -> None:
        """Person eats and increases satiety."""
        if self.house.food >= 10:
            print(f'{self.name} ate')
            self.satiety += 20
            self.house.remove_food(10)
        else:
            print(f'{self.name} has no food in the house')

    def work(self) -> None:
        """Person goes to work and earns money."""
        print(f'{self.name} went to work')
        self.satiety -= 10
        self.house.add_money(50)

    def play(self) -> None:
        """Person plays, reducing their satiety."""
        print(f'{self.name} played')
        self.satiety -= 10

    def go_shopping(self) -> None:
        """Person goes shopping for food."""
        if self.house.money >= 50:
            print(f'{self.name} went shopping')
            self.house.add_food(50)
            self.house.remove_money(50)
        else:
            print(f'{self.name} has no money in the house')

    def act(self) -> None:
        """Decides what action the person should take."""
        dice = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()
