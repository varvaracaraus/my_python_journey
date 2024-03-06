# Digit Counter
# This script counts the number of digits in a given number by repeatedly dividing the number by 10.

# Input for the number
number = int(input('Enter your number: '))

# Initialize the digit count
digit_count = 0

# Count the number of digits
while number > 0:
    number = number // 10
    digit_count += 1

# Print the count of digits
print(digit_count)
