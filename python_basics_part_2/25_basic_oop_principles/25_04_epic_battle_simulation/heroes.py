import random


class Hero:
    """ A class representing a generic hero with health, power, and survival abilities. """

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        """ Initialize a Hero with a name and default health and power. """
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        """ Return the current health of the Hero. """
        return self.__hp

    def set_hp(self, new_value):
        """ Set the Hero's health to a new value, ensuring it doesn't go below 0. """
        self.__hp = max(new_value, 0)

    def get_power(self):
        """ Return the current power of the Hero. """
        return self.__power

    def set_power(self, new_power):
        """ Set the Hero's power to a new value. """
        self.__power = new_power

    def is_alive(self):
        """ Check if the Hero is still alive. """
        return self.__is_alive

    def attack(self, target):
        """ Raise an error to remind to override this method in subclasses. """
        raise NotImplementedError("You forgot to override the attack method!")

    def take_damage(self, damage):
        """ Apply damage to the Hero and check if they're still alive. """
        print("\t", self.name, "took a hit with force equal to = ", round(damage),
              ". Remaining health - ", round(self.get_hp()))
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        """ Increment the Hero's power slightly. """
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        """ Raise an error to remind to override this method in subclasses. """
        raise NotImplementedError("You forgot to override the __str__ method!")


class Healer(Hero):
    """ A subclass of Hero specialized in healing allies. """

    def __init__(self, name):
        """ Initialize the Healer with enhanced magic power. """
        super().__init__(name)
        self.magic_power = self.start_power * 3

    def attack(self, target):
        """ Attack a target with halved power. """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        """ Take more damage than usual. """
        super().take_damage(damage * 1.2)

    def heal(self, target):
        """ Heal a target with the Healer's magic power. """
        target.set_hp(target.get_hp() + self.magic_power)

    def make_a_move(self, friends, enemies):
        """ Decide between healing a friend or attacking an enemy. """
        if random.random() < 0.5:
            target_friend = random.choice(friends)
            self.heal(target_friend)
        else:
            if enemies:
                target_enemy = random.choice(enemies)
                self.attack(target_enemy)

    def __str__(self):
        """ Return a string representation of the Healer. """
        return f"Healer {self.name}: Health = {self.get_hp()}, Power = {self.get_power()}"


class Tank(Hero):
    """ A subclass of Hero specialized in defense with a shield. """

    def __init__(self, name):
        """ Initialize the Tank with a defense mechanism. """
        super().__init__(name)
        self.defense = 1
        self.shield_up = False

    def attack(self, target):
        """ Attack a target with halved power. """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        """ Reduce damage taken if shield is up. """
        if self.shield_up:
            damage /= self.defense
        super().take_damage(damage)

    def raise_shield(self):
        """ Raise the shield to double the defense. """
        self.shield_up = True
        self.defense *= 2

    def lower_shield(self):
        """ Lower the shield and revert the defense. """
        self.shield_up = False
        self.defense /= 2

    def make_a_move(self, friends, enemies):
        """ Decide between raising the shield or attacking. """
        if self.get_hp() < Hero.max_hp * 0.5 and not self.shield_up:
            if random.random() < 0.7:
                self.raise_shield()
            else:
                if enemies:
                    target_enemy = random.choice(enemies)
                    self.attack(target_enemy)
        elif self.shield_up:
            if random.random() < 0.5:
                self.lower_shield()
            else:
                if enemies:
                    target_enemy = random.choice(enemies)
                    self.attack(target_enemy)
        else:
            if enemies:
                target_enemy = random.choice(enemies)
                self.attack(target_enemy)

    def __str__(self):
        """ Return a string representation of the Tank. """
        shield_status = "up" if self.shield_up else "down"
        return (f"Tank {self.name}: Health = {self.get_hp()}, "
                f"Power = {self.get_power()}, Shield = {shield_status}")


class Attacker(Hero):
    """ A subclass of Hero specialized in offensive attacks. """

    def __init__(self, name):
        """ Initialize the Attacker with a power multiplier. """
        super().__init__(name)
        self.power_multiply = 1

    def attack(self, target):
        """ Attack a target with multiplied power. """
        target.take_damage(self.get_power() * self.power_multiply)

    def take_damage(self, damage):
        """ Take more damage the higher the power multiplier. """
        super().take_damage(damage * (self.power_multiply / 2))

    def power_up(self):
        """ Double the power multiplier. """
        self.power_multiply *= 2

    def power_down(self):
        """ Halve the power multiplier. """
        self.power_multiply /= 2

    def make_a_move(self, friends, enemies):
        """ Decide between powering up or attacking. """
        if self.get_hp() > Hero.max_hp * 0.75:
            if random.random() < 0.5:
                self.power_up()
            else:
                if enemies:
                    target_enemy = random.choice(enemies)
                    self.attack(target_enemy)
        else:
            if random.random() < 0.3:
                self.power_down()
            else:
                if enemies:
                    target_enemy = random.choice(enemies)
                    self.attack(target_enemy)

    def __str__(self):
        """ Return a string representation of the Attacker. """
        return (f"Attacker {self.name}: Health = {self.get_hp()}, "
                f"Power = {self.get_power()}, Multiplier = {self.power_multiply}")
