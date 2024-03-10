# Video Card List Updater
# This script takes a number of video card values as input, removes the video card with the highest value
# and displays the new list.

# Reading the number of video cards
quantity = int(input('Number of video cards: '))

# Lists for storing video card values
video_cards = []
new_cards = []

# Collecting video card values
for i in range(1, quantity + 1):
    card = int(input(f"Video card {i}: "))
    video_cards.append(card)
print('\nOld video card list:', video_cards)

# Finding the maximum value among the video cards
max_value = video_cards[0]
for card in video_cards:
    if card > max_value:
        max_value = card

# Creating a new list without the max value
for card in video_cards:
    if card != max_value:
        new_cards.append(card)

# Displaying the new list of video cards
print('New list of video cards:', new_cards)
