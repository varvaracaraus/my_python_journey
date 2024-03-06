# Speeding Fine Calculation System
# This script calculates the fine for speeding based on whether the vehicle is in town or country
# and the amount by which the speed limit is exceeded.

# Constants for fine amounts
FINE_1_TO_10 = 30
FINE_11_TO_15 = 50
FINE_16_TO_20 = 70
FINE_21_TO_25 = 115
FINE_26_TO_30 = 180
FINE_31_TO_40 = 260
FINE_41_TO_50 = 400
FINE_51_TO_60 = 560
FINE_61_TO_70 = 700
FINE_OVER_70 = 800

# Speed limits
TOWN_SPEED_LIMIT = 50
COUNTRY_SPEED_LIMIT = 70

# Vehicle speed and location
vehicle_speed = 111
is_in_town = True

# Calculate over speed
if is_in_town:
    over_speed = vehicle_speed - TOWN_SPEED_LIMIT
else:
    over_speed = vehicle_speed - COUNTRY_SPEED_LIMIT

# Initialize fine
fine = 0

# Determine the fine based on over speed
if over_speed < 1:
    print("Speed not exceeded or exceeded insignificantly")
elif 1 <= over_speed < 10:
    fine = FINE_1_TO_10
elif 11 <= over_speed < 15:
    fine = FINE_11_TO_15
elif 16 <= over_speed < 20:
    fine = FINE_16_TO_20
elif 21 <= over_speed < 25:
    fine = FINE_21_TO_25
elif 26 <= over_speed < 30:
    fine = FINE_26_TO_30
elif 31 <= over_speed < 40:
    fine = FINE_31_TO_40
elif 41 <= over_speed < 50:
    fine = FINE_41_TO_50
elif 51 <= over_speed < 60:
    fine = FINE_51_TO_60
elif 61 <= over_speed < 70:
    fine = FINE_61_TO_70
elif over_speed >= 70:
    fine = FINE_OVER_70

# Print the result
if fine > 0:
    print("Fine: " + str(fine))
else:
    print("Speed not exceeded or exceeded insignificantly")
