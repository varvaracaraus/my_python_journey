# Theater Layout Visualizer
# This script creates a visual representation of a theater layout, taking into account the number of rows, 
# the number of seats in each row, and the distance between rows.

# Input for the number of rows, seats per row, and distance between rows
total_rows = int(input('Enter the number of rows: '))
seats_per_row = int(input('Enter the number of seats in a row: '))
distance_between_rows = int(input('Enter the number of meters between rows: '))

# Loop to print the layout of each row
for row in range(total_rows):
    print('=' * seats_per_row, ' ' * distance_between_rows, '=' * seats_per_row)
