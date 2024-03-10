# Function Value Calculator
# This script calculates the value of a function based on the input value of x. 
# The function is defined as follows: y = x - 12 if x > 0; y = 5 if x = 0; y = x^2 if x < 0.

# Input for x value
x_value = int(input('Enter x value: '))

# Calculate the function's value based on x
if x_value > 0:
    y_value = x_value - 12
elif x_value == 0:
    y_value = 5
else:
    y_value = x_value ** 2

# Print the result
print('y =', y_value)
