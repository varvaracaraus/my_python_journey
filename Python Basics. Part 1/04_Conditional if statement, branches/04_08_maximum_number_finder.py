# Maximum Number Finder
# This script prompts the user to enter three numbers and determines the maximum among them.

# Input for three numbers
first_number = int(input('Enter the 1st number: '))
second_number = int(input('Enter the 2nd number: '))
third_number = int(input('Enter the 3rd number: '))

# Determine and print the maximum number
if first_number >= second_number and first_number >= third_number:
    print('Maximum number:', first_number)
elif second_number >= first_number and second_number >= third_number:
    print('Maximum number:', second_number)
else:
    print('Maximum number:', third_number)
