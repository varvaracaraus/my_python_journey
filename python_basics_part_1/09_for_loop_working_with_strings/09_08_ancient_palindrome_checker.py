# Ancient Palindrome Checker
# This script checks if the entered message is a palindrome. A palindrome is a word, phrase,
# number, or other sequence of characters that reads the same forward and backward.

# Input for the message
original_message = input('Enter the message: ')

# Initialize a string to store the reversed message
reversed_message = ''

# Reverse the message
for char in original_message:
    reversed_message = char + reversed_message

# Check if the message is a palindrome and print the result
if reversed_message == original_message:
    print('Yes, this is a palindrome!')
else:
    print('No, this is not a palindrome!')
