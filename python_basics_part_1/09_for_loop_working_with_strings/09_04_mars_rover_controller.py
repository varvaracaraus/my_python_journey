# Mars Rover Controller
# This script simulates the control of a Mars rover named Billy. The user can move Billy north (N), south (S),
# west (W), or east (E) within a specified grid limit.

print('To control Billy, enter:\nNorth (N key), South (S key), West (W key), or East (E key).')

# Initialize Billy's starting position
x_position = 8
y_position = 10

# Define grid limits
x_limit = 15
y_limit = 20

# Loop to control Billy's movements
while True:
    command = input(f"\nBilly's location is: x={x_position}, y={y_position}.\nEnter the command: ")
    if command == 'N' and y_position < y_limit:
        y_position += 1
    elif command == 'S' and y_position > 0:
        y_position -= 1
    elif command == 'W' and x_position > 0:
        x_position -= 1
    elif command == 'E' and x_position < x_limit:
        x_position += 1
