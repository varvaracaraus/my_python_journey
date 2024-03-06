# Clock
# This script converts a number of minutes into hours and remaining minutes.

# Input for the number of minutes
minutes = int(input('Enter the number of minutes: '))

# Calculate hours and remaining minutes
hours = minutes // 60
remaining_minutes = minutes % 60

# Print the hours and remaining minutes
print('Hours:', hours)
print('Remaining minutes:', remaining_minutes)
