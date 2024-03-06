# Parcel Collection Availability
# This script determines if a parcel can be received based on the hour of the day. 
# Parcel collection is unavailable during certain hours (0-8, 10-18, 22-23).

# Input for the current hour
current_hour = int(input('Enter the hour: '))

# Check availability and print the result
if ((0 <= current_hour < 8) or
        (10 <= current_hour < 18) or
        (22 <= current_hour <= 23)):
    print('The parcel cannot be received.')
else:
    print('You can receive the parcel.')
