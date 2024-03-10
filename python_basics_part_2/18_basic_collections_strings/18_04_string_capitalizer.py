# String Capitalizer
# This script capitalizes the first letter of each word in a user-input string.

# Taking user input for a string
user_input = input("Enter a string: ")

# Capitalizing the first letter of each word in the string
result = ' '.join(word.capitalize() for word in user_input.split())

# Displaying the capitalized result
print(f'Result: {result}')
