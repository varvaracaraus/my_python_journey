# Script to generate a list of odd numbers from 1 to a given number

# Initialize an empty list to hold odd numbers
odd_list = []

# User input for the number
num = int(input('Enter the number: '))

# Iterate through numbers from 1 to num (inclusive) and append odd numbers to the list
for i in range(num + 1):
    if i % 2 == 1:
        odd_list.append(i)

# Print the list of odd numbers
print(f'List of odd numbers from one to {num}: {odd_list}')
