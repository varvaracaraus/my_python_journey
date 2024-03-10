# Splitting a Number into Parts
# This script takes a four-digit number as input and prints each of its digits separately.

# Input for a four-digit number
four_digit_number = int(input('Enter a four-digit number: '))

# Extract and print each digit
thousands_digit = (four_digit_number % 10000) // 1000
hundreds_digit = (four_digit_number % 1000) // 100
tens_digit = (four_digit_number % 100) // 10
ones_digit = four_digit_number % 10

# Print each digit on a separate line
print(thousands_digit)
print(hundreds_digit)
print(tens_digit)
print(ones_digit)
