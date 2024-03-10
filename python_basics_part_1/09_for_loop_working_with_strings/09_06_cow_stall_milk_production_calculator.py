# Cow Stall Milk Production Calculator
# This script calculates the total milk production per day based on the status of 10 stalls in a barn.
# Each stall contributes 2 more units of milk than the previous stall. 'a' indicates a free stall,
# and 'b' indicates an occupied stall.

# Input for the status of all 10 stalls
stall_status = input('Enter the status of all 10 stalls (a — if free, b — if occupied): ')

# Initialize the variables for milk increment and total milk production
milk_increment = 0
total_milk_produced = 0

# Calculate total milk production based on stall status
for stall in stall_status:
    milk_increment += 2
    if stall == 'b':
        total_milk_produced += milk_increment

# Print the total milk produced per day
print('Milk produced per day:', total_milk_produced)
