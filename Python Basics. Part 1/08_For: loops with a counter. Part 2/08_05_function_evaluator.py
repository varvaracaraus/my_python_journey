# Function Evaluator
# This script evaluates the function y = x^3 + 2x^2 - 4x + 1 for each point in a specified range and step.
# The user inputs the lower limit, upper limit, and the step value for the evaluation.

# Input for the range and step
lower_limit = int(input('Enter the lower limit: '))
upper_limit = int(input('Enter the upper limit: '))
step = int(input('Enter the step: '))

# Adjust limits and step if the step is negative
if step < 0:
    lower_limit, upper_limit = upper_limit, lower_limit - 1  # Inclusive of upper_limit for negative step
else:
    upper_limit += 1  # Exclusive of upper_limit for positive step

# Evaluate and print the function for each point in the range
for point in range(lower_limit, upper_limit, step): 
    y = (point ** 3) + (2 * (point ** 2)) - (4 * point) + 1
    print(f'At point {point}, the function is equal to {y}')
