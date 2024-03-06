# Pyramid with Increasing Odd Numbers
# This script prints a pyramid pattern with increasing odd numbers. The numbers increase as they go up 
# each level of the pyramid, and spaces are used to align the numbers symmetrically.

# Input for the number of pyramid levels
pyramid_levels = int(input('Enter the number of pyramid levels: '))
count = -1

# Loop through each level of the pyramid
for row in range(1, pyramid_levels + 1):
    # Print spaces for alignment
    for _ in range(pyramid_levels - row):
        print(" ", end='\t')

    # Print the left side of the pyramid
    for left_side in range(1, row + 1):
        if left_side % 2 != 0:
            count += 2
            print(count, end='\t')
        else:
            print(' ', end='\t')

    # Print the right side of the pyramid
    for right_side in range(row - 1, 0, -1):
        if right_side % 2 != 0:
            count += 2
            print(count, end='\t')
        else:
            print(' ', end='\t')

    # Move to the next line after each row
    print()
