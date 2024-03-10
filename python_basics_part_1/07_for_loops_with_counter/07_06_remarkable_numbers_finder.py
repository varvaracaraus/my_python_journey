# Remarkable Numbers Finder
# This script finds and prints a two-digit number that meets the condition:
# (tens digit * units digit * 3) equals the number itself. The user enters the starting number for the search.

# Input for the starting number
input_number = int(input('Enter the starting number for the search: '))

# Loop through the range of two-digit numbers
for number in range(10, 100):
    product = (number // 10) * (number % 10) * 3
    if product == input_number:
        print('Remarkable number found:', number)
        break
else:
    print('No remarkable number found.')
