# Number Pattern Printer
# This script prints a specific pattern of numbers in a table format. Each row starts with a 
# base number (from 0 to 5), and each column value is increased by a step of 2.

# Loop through the rows
for row in range(6):
    # Loop through the columns with a step of 2
    for col in range(0, 11, 2):
        # Print the column value on the first row and row + column value on other rows
        if row == 0:
            print(col, end='\t')
        else:
            print(row + col, end='\t')
    # Move to the next line after each row
    print()
