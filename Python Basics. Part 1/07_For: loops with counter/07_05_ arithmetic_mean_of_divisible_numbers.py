# Arithmetic Mean of Divisible Numbers
# This script calculates the arithmetic mean of all numbers divisible by 3 in a given range,
# specified by two numbers entered by the user.

# Input for the start and end of the range
start_number = int(input('Enter the 1st number: '))
end_number = int(input('Enter the 2nd number: '))

# Initialize the sum and count of numbers divisible by 3
total_sum = 0
count_divisible_by_three = 0

# Calculate the sum and count of numbers divisible by 3
for number in range(start_number, end_number + 1):
    if number % 3 == 0:
        total_sum += number
        count_divisible_by_three += 1

# Calculate and print the arithmetic mean
if count_divisible_by_three > 0:
    arithmetic_mean = total_sum / count_divisible_by_three
    print('Arithmetic mean =', arithmetic_mean)
else:
    print('No numbers divisible by 3 in the range.')
