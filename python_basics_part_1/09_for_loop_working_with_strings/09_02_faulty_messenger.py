# Faulty Messenger
# This script identifies the position of the first '*' symbol in a message entered by the user.

# Input for the message with an error
error_message = input('Enter the message that contains the error: ')

# Search for the '*' symbol and print its position
for position, symbol in enumerate(error_message):
    if symbol == '*':
        print('The "*" symbol is at position', position + 1)
        break
else:
    print('No "*" symbol found in the message.')
