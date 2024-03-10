# List Shifter
# This script shifts the elements of a list by a specified number of positions.
# Positive shift values move elements to the right, while negative values shift them to the left.

# Creating an empty list
input_list = []

# Reading the number of elements to be added to the list
symbols = int(input('Enter how many numbers in list: '))

# Collecting numbers for the list
for symbol in range(symbols):
    num = int(input(f'Enter {symbol + 1} number: '))
    input_list.append(num)

# Reading the number of positions for shifting
steps = int(input('By how many positions to shift: '))
print('Initial list:', input_list)

# Shifting the list
if steps > 0:
    for i in range(steps):
        input_list.insert(0, input_list.pop())
elif steps < 0:
    for i in range(abs(steps)):
        input_list.append(input_list.pop(0))

print('Shifted list:', input_list)
