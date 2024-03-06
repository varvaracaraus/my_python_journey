# Dice Game
# In this game, the guest and the owner each roll a dice. If the guest's dice roll is greater than
# or equal to the owner's, the guest pays. Otherwise, their rolls are summed and the owner pays.
# The game ends with a closing message.

# Input for each player's dice roll
guests_dice_roll = int(input('Guests dice: '))
owners_dice_roll = int(input('Owners dice: '))

# Determine the outcome of the game
if guests_dice_roll >= owners_dice_roll:
    print('Guests dice is bigger or is the same.')
    print('Guest pays.')
else:
    print('Sum:', guests_dice_roll + owners_dice_roll)
    print('Owner pays.')

print('Game over!')
