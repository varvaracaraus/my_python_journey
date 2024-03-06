# Largest Number Finder
# This script takes two numbers as input and determines the larger number without using
# conventional conditional statements.

# Input for the two numbers
first_number = float(input('Enter the 1st number: '))
second_number = float(input('Enter the 2nd number: '))

# Calculate the difference and determine which number is larger
difference = first_number - second_number
is_first_larger = (difference // abs(difference) + 1) // 2
larger_number = first_number * is_first_larger + second_number * (1 - is_first_larger)

# Print the larger number
print("The largest number is:", int(larger_number))
