# Arithmetic Mean of Multiples
# This script calculates the arithmetic mean of all numbers in a specified interval (a, b)
# that are multiples of a given number c.

# Input for the interval start, end, and the multiple
start_number = int(input('Enter the 1st number: '))
end_number = int(input('Enter the 2nd number: '))
multiple = int(input('Enter the 3rd number: '))

# Initialize the sum and count of numbers that are multiples of 'c'
total_sum = 0
multiples_count = 0

# Calculate the sum and count of multiples of 'c'
for number in range(start_number, end_number):
    if number % multiple == 0:
        total_sum += number
        multiples_count += 1

# Calculate and print the arithmetic mean, if applicable
if multiples_count > 0:
    arithmetic_mean = total_sum / multiples_count
    print(f'The arithmetic mean of numbers in the interval from {start_number} to '
          f'{end_number} that are multiples of {multiple} is equal to {arithmetic_mean}')
else:
    print(f'There are no numbers in the specified interval from {start_number} to '
          f'{end_number} that are multiples of {multiple}')
