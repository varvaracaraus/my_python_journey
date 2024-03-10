# Number Staircase Printer
# This script prints a staircase pattern of numbers. The number in each row increases and equals the row number.

# Input for the size of the staircase
staircase_size = int(input('Enter the size of the staircase: '))

# Loop through each row
for row in range(1, staircase_size + 1):
    # Loop through each column
    for col in range(1, staircase_size + 1):
        # Print the row number if the row index is greater than or equal to the column index
        if row >= col:
            print(row, end='\t')
    # Move to the next line after each row
    print()
