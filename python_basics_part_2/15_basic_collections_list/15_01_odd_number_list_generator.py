# Odd Number List Generator
# This script generates a list of odd numbers from 1 up to the user-input number and displays it.

# List to store odd numbers
odd_list = []

# Taking input from the user
num = int(input('Enter the number: '))

# Generating odd numbers up to the input number
for i in range(num + 1):
    if i % 2 == 1:
        odd_list.append(i)

# Displaying the list of odd numbers
print(f'List of odd numbers from 1 to {num}: {odd_list}')
