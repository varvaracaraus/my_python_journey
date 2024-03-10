# Main Script for Simulating a Battle
# This script creates warriors and initiates a battle between them.

from battle import Battle  # Importing the Battle class
from warrior import Warrior  # Importing the Warrior class

# Creating warriors
warrior1 = Warrior("Warrior 1")  # Creating the first warrior
warrior2 = Warrior("Warrior 2")  # Creating the second warrior

# Initiating the battle
battle = Battle(warrior1, warrior2)  # Creating a Battle instance with the two warriors
battle.start_battle()  # Starting the battle
