# Frame Printer
# This script prints a rectangular frame with a specified height and width.
# The frame is represented by '|' on the sides and '-' on the top and bottom.

# Input for the frame's dimensions
frame_height = int(input("Enter the frame's height: "))
frame_width = int(input("Enter the frame's width: "))

# Loop through each row
for row in range(frame_height):
    # Loop through each column
    for col in range(frame_width):
        # Print '|' for the sides of the frame
        if col == 0 or col == frame_width - 1:
            print('|', end='')
        # Print '-' for the top and bottom of the frame
        elif row == 0 or row == frame_height - 1:
            print('-', end=' ')
        # Print spaces for the inside of the frame
        else:
            print(' ', end=' ')
    # Move to the next line after each row
    print()
