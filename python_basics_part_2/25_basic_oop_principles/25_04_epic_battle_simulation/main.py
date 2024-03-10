import random

from heroes import Tank, Healer, Attacker
from monsters import MonsterBerserk, MonsterHunter


def one_year_of_war():
    """ Simulate a year of war between a team of heroes and a team of monsters. """

    # Initializing heroes
    tank = Tank("Arthur the Guardian")
    healer = Healer("Grace the Lifesaver")
    attacker1 = Attacker("Edward the Stormbringer")
    attacker2 = Attacker("Isabel the Inferno")

    good_team = [tank, healer, attacker1, attacker2]

    # Ensure that there is at most one monster in the heroes team
    if sum([isinstance(hero, (MonsterHunter, MonsterBerserk)) for hero in good_team]) > 1:
        print("There can only be one monster in the heroes' team!")
        return 0

    # Names of the evil team members
    evil_names = ["Grimshaw", "Ravenor", "Vexx", "Necros", "Shadowmist", "Ironclad"]
    mob_warrior = MonsterBerserk("Berserk " + random.choice(evil_names))
    mob_ranger = MonsterHunter("Ranger " + random.choice(evil_names))
    evil_team = [mob_warrior, mob_ranger]

    for day in range(1, 366):
        print("=" * 50 + "\nStart of day #" + str(day) + "\n" + "=" * 50)

        # Heroes' actions
        print("\nHeroes' team:\n" + '-' * 50)
        for hero in good_team:
            hero.make_a_move(good_team, evil_team)

        # Monsters' actions
        print("\nEvil team:\n" + '-' * 50)
        for mob in evil_team:
            mob.make_a_move(evil_team, good_team)

        print(f"End of day #{day} battles")

        # Status update
        print("\nHeroes' team:\n" + '-' * 50)
        for hero in good_team:
            print(hero)

        print("\nEvil team:\n" + '-' * 50)
        for mob in evil_team:
            print(mob)

        # Update evil team
        evil_team = [mob for mob in evil_team if mob.is_alive()]
        if day % 2 == 0 and len(evil_team) < 4:
            newborn_evils = [
                MonsterBerserk("Berserk " + random.choice(evil_names)),
                MonsterHunter("Ranger " + random.choice(evil_names))
            ]
            evil_team.append(random.choice(newborn_evils))

        # Check if heroes are still alive
        if any([not hero.is_alive() for hero in good_team]):
            print("You have lost!")
            return 0
        else:
            print("The battle continues!")

    else:
        print("You have won!")
        return 1


# Counting the number of victories over 20 years
count_of_wins = 0
for year in range(1, 21):
    count_of_wins += one_year_of_war()

# Reporting the outcome
print("Out of 20 times, the heroes' team won", count_of_wins, "times")
if count_of_wins < 10:
    print("The heroes need a different strategy, try again!")
else:
    print("The heroes are ready for the real battle, mission accomplished!")
