# Pit Pattern Printer
# This script prints a pattern resembling a pit with numbers and dots.
# The numbers decrease from the input number at the edges towards the center, where they are replaced by dots.

# Input for the number that forms the base of the pit pattern
number = int(input('Enter the number: '))

# Loop to construct each row of the pattern
row = number
while row >= 0:
    # Print decreasing numbers from the input number to row
    col = number
    while col > row:
        print(col, end='')
        col -= 1

    # Print dots in the center
    col = 1
    while row < number and col <= 2 * row:
        print('.', end='')
        col += 1

    # Print increasing numbers from row to the input number
    col = row + 1
    while col <= number:
        print(col, end='')
        col += 1

    # Move to the next line after each row
    print()
    row -= 1
