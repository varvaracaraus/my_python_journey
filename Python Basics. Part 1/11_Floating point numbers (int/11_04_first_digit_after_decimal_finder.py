# First Digit After Decimal Finder
# This script takes a number as input and prints the first digit after the decimal point.

# Input for the number
input_number = float(input('Enter the number: '))

# Calculate the first digit after the decimal point
first_digit_after_decimal = int(input_number * 10) % 10

# Print the result
print('The first digit after the decimal point is:', first_digit_after_decimal)
