# Accountant Verification
# This script checks an accountant's calculations by summing the last two digits of two numbers.

# Input for two numbers
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))

# Calculate the last two digits of each number
first_number_last_two_digits = first_number % 100
second_number_last_two_digits = second_number % 100

# Calculate and print the sum of the last two digits
sum_of_last_two_digits = first_number_last_two_digits + second_number_last_two_digits
print('Sum of last two digits:', sum_of_last_two_digits)
