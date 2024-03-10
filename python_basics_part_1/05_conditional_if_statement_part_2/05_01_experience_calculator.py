# Experience Calculator
# This script takes the amount of accumulated points as input and calculates the user's level
# based on these points.

# Input for the amount of accumulated points
accumulated_points = int(input('Enter the amount of accumulated points: '))

# Determine and print the user's level
if accumulated_points < 1000:
    print('Your level is: 1')
elif accumulated_points < 2500:
    print('Your level is: 2')
elif accumulated_points < 5000:
    print('Your level is: 3')
else:
    print('Your level is: 4')
