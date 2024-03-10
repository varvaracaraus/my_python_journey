# Swap Numbers
# This script swaps the values of two numbers without using a temporary variable.

# Input for two numbers
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))

# Print original numbers
print("Original order:", first_number, second_number)

# Swapping the numbers
first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

# Print swapped numbers
print("Swapped order:", first_number, second_number)
