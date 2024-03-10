import random


class Monster:
    """ A class representing a generic monster with health and power attributes. """

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        """ Initialize a Monster with a name and default health and power. """
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        """ Return the current health of the Monster. """
        return self.__hp

    def set_hp(self, new_value):
        """ Set the Monster's health to a new value, ensuring it doesn't go below 0. """
        self.__hp = max(new_value, 0)

    def get_power(self):
        """ Return the current power of the Monster. """
        return self.__power

    def set_power(self, new_power):
        """ Set the Monster's power to a new value. """
        self.__power = new_power

    def attack(self, target):
        """ Placeholder for attack method to be implemented in subclasses. """
        pass

    def is_alive(self):
        """ Check if the Monster is still alive. """
        return self.__is_alive

    def take_damage(self, damage):
        """ Apply damage to the Monster and check if it's still alive. """
        print("\t", self.name, "took damage with a force equal to = ",
              round(damage), ". Remaining health - ", round(self.get_hp()))
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        """ Placeholder for making a move, to be implemented in subclasses. """
        pass

    def __str__(self):
        """ Return a string representation of the Monster. """
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())


class MonsterBerserk(Monster):
    """ A subclass of Monster that goes into a berserk state when attacking. """

    def __init__(self, name):
        """ Initialize the MonsterBerserk with an additional madness attribute. """
        super().__init__(name)
        self.madness = 1

    def attack(self, target):
        """ Attack a target with power multiplied by madness. Increase madness after attack. """
        target.take_damage(self.get_power() * self.madness)
        self.madness += 0.1

    def take_damage(self, power):
        """ Take damage and increase madness if health goes below 50. """
        self.set_hp(self.get_hp() - power * (self.madness / 2))
        if self.get_hp() < 50:
            self.madness *= 2
        super().take_damage(power)

    def make_a_move(self, friends, enemies):
        """ Make a move during the battle, attack based on madness level. """
        print(self.name, end=' ')
        self.madness = min(self.madness, 4)
        if not enemies:
            return
        if self.madness < 3:
            print("Attacking the nearest -", enemies[0].name)
            self.attack(enemies[0])
        else:
            target = random.choice(enemies)
            print("BERSERK MODE!!! Madness level - " + str(self.madness) + " Randomly attacking -", target.name)
            print()
            self.attack(target)
        print('\n')


class MonsterHunter(Monster):
    """ A subclass of Monster that has healing potions and can heal friends. """

    def __init__(self, name):
        """ Initialize the MonsterHunter with potions. """
        super().__init__(name)
        self.potions = 10

    def attack(self, target):
        """ Attack a target with additional power based on remaining potions. """
        target.take_damage(self.get_power() + (10 - self.potions))

    def take_damage(self, power):
        """ Take damage and randomly use a potion to heal. """
        self.set_hp(self.get_hp() - power)
        if random.randint(1, 10) == 1:
            self.potions -= 1
        super().take_damage(power)

    def give_a_potion(self, target):
        """ Give a potion to a friend, increasing their health. """
        self.potions -= 1
        target.set_hp(target.get_hp() + self.get_power())

    def make_a_move(self, friends, enemies):
        """ Make a move during the battle, either heal a friend or attack an enemy. """
        print(self.name, end=' ')
        target_of_potion = friends[0]
        min_health = target_of_potion.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_potion = friend
                min_health = target_of_potion.get_hp()

        if min_health < 60 and self.potions > 0:
            print("Healing", target_of_potion.name)
            self.give_a_potion(target_of_potion)
        else:
            if not enemies:
                return
            print("Attacking the nearest -", enemies[0].name)
            self.attack(enemies[0])
        print('\n')
