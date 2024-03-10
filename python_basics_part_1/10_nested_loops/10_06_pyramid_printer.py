# Pyramid Printer
# This script prints a pyramid of a specified height. The pyramid is made of '#' symbols and is centered.

# Input for the pyramid height
pyramid_height = int(input('Enter pyramid height: '))

# Loop through each row of the pyramid
for row in range(pyramid_height):
    # Loop through each column position for the row
    for col in range((pyramid_height * 2) - 1):
        # Print '#' for the pyramid part and spaces for the rest
        if pyramid_height - row - 1 <= col <= pyramid_height + row - 1:
            print('#', end='')
        else:
            print(' ', end='')
    # Move to the next line after each row
    print()
