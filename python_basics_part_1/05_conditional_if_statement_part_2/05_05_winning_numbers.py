# Winning Numbers
# This script takes three numbers as input and determines how many of them match. 
# It then prints the count of matching numbers.

# Input for three numbers
first_number = int(input('Enter the 1st number: '))
second_number = int(input('Enter the 2nd number: '))
third_number = int(input('Enter the 3rd number: '))

# Determine the number of matching numbers and print the result
if first_number == second_number and second_number == third_number:
    print('Number of matching numbers: 3')
elif first_number == second_number or second_number == third_number or first_number == third_number:
    print('Number of matching numbers: 2')
else:
    print('All numbers are different: 0')
