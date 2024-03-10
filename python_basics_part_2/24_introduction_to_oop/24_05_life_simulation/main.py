from house import House
from person import Person


def simulate_life(days: int) -> None:
    """
    Simulate the life of persons for a given number of days.

    Args:
        days (int): The number of days to simulate.
    """
    house = House()
    person1 = Person("Roma", house)
    person2 = Person("Varea", house)

    for day in range(1, days + 1):
        print(f'\nDay {day}:')
        print("Morning status:")
        print(f"Money in house: {house.money}")
        print(f"Food in house: {house.food}")
        print(person1)
        print(person2)
        person1.act()
        person2.act()
        print(f'Food left in the house: {house.food}, money: {house.money}')
        if person1.satiety <= 0:
            print(f'{person1.name} died of starvation')
            break
        if person2.satiety <= 0:
            print(f'{person2.name} died of starvation')
            break


# Directly call the function
simulate_life(365)
