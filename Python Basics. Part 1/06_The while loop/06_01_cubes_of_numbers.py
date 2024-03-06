# Cubes of Numbers
# This script prints the cubes of all numbers from 1 up to the specified number.

# Input for the number up to which cubes will be printed
limit_number = int(input('Enter the number: '))

# Initialize the counter
counter = 1

# Print the cubes of numbers from 1 to limit_number
while counter <= limit_number:
    print(f'For the number {counter} power of three = {counter ** 3}')
    counter += 1
