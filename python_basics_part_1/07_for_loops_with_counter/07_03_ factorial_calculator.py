# Factorial Calculator
# This script calculates the factorial of a given number. The factorial of a number n is the product
# of all positive integers less than or equal to n.

# Input for the number
number = int(input('Enter the number: '))

# Initialize the factorial result
factorial_result = 1

# Loop to calculate the factorial
for i in range(2, number + 1):
    factorial_result *= i

# Print the factorial
print('Factorial of the number is:', factorial_result)
