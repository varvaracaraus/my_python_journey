# Rough Mathematics
# This script asks the user to input a sequence of real numbers. For each positive number, it calculates
# and prints the natural logarithm of its ceiling. For each non-positive number, it calculates and prints
# the exponential function of its floor value.

import math

# Input for the number of real numbers
number_of_elements = int(input('Enter the number of real numbers: '))

# Process each number in the sequence
for _ in range(number_of_elements):
    number = float(input('\nEnter the number: '))
    if number > 0:
        x = math.ceil(number)
        print('x =', x, '    log(x) =', math.log(x))
    else:
        x = math.floor(number)
        print('x =', x, '    exp(x) =', math.exp(x))
