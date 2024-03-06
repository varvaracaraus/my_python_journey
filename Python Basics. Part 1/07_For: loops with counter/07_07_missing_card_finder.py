# Missing Card Finder
# This script asks the user for the total number of cards and then for the numbers of each remaining card.
# It calculates and prints the number of the missing card.

# Input for the total number of cards
total_cards = int(input('Enter the total number of cards: '))

# Initialize the sum of total card numbers and the sum of remaining card numbers
sum_of_card_numbers = 0
sum_of_remaining_cards = 0

# Loop to collect the numbers of the remaining cards
for card_number in range(1, total_cards):
    sum_of_card_numbers += card_number
    remaining_card = int(input('Enter the number of the remaining card: '))
    sum_of_remaining_cards += remaining_card

# Add the number of the last card to the sum of card numbers
sum_of_card_numbers += total_cards

# Calculate and print the missing card number
missing_card_number = sum_of_card_numbers - sum_of_remaining_cards
print('Missing card number is:', missing_card_number)
