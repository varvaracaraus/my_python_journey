# Largest Digit Sum Finder
# This script asks the user to input a sequence of integers and then finds the number that has
# the largest sum of its digits.

# Input for the number of integers in the sequence
number_of_integers = int(input('Enter the number of integers: '))

# Initialize variables to track the maximum sum and the corresponding number
max_digit_sum = 0
number_with_max_sum = 0

# Loop through each number in the sequence
for i in range(number_of_integers):
    current_number = int(input(f'Enter number {i + 1}: '))
    temp_number = current_number
    digit_sum = 0

    # Calculate the sum of digits of the current number
    while temp_number > 0:
        digit_sum += temp_number % 10
        temp_number //= 10

    # Update the maximum digit sum and the corresponding number
    if digit_sum > max_digit_sum:
        max_digit_sum = digit_sum
        number_with_max_sum = current_number

# Print the result
print(f'The number {number_with_max_sum} has the largest sum of digits: {max_digit_sum}')
