# Video Card Filter
# This script reads a list of video card values, finds the maximum value, and creates a new list excluding
# the video card with that maximum value.

# Input for the number of video cards
quantity = int(input('Number of video cards: '))

# Initialize lists for storing video card values
video_cards = []
new_cards = []

# Read video card values and populate the video_cards list
for i in range(1, quantity + 1):
    card = int(input(f"Video card {i}: "))
    video_cards.append(card)
print('\nOld video card list:', video_cards)

# Find the maximum value among the video cards
max_value = max(video_cards)

# Create a new list excluding the video card with the maximum value
new_cards = [card for card in video_cards if card != max_value]

# Print the new list of video cards
print('New list of video cards:', new_cards)
