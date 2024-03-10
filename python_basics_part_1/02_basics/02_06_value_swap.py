# Value Swap
# This script takes two words as input from the user and then swaps their values.

# Get two words from the user
first_word = input('Enter the first word: ')
second_word = input('Enter the second word: ')

# Print the original order of words
print(first_word, second_word)

# Swapping the values of the words
temp = first_word
first_word = second_word
second_word = temp

# Print the words after swapping
print(first_word, second_word)
