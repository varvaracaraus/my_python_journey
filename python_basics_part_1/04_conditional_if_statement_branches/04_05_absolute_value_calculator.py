# Absolute Value Calculator
# This script calculates the absolute value of a given number.

# Input for the number
number = int(input('Enter the number: '))

# Calculate and print the absolute value
if number >= 0:
    print('The absolute value of the number is:', number)
else:
    abs_number = -number
    print('The absolute value of the number is:', abs_number)
