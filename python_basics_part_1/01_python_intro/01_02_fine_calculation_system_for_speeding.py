# Fine Calculation System for Speeding
# This script calculates the fine for speeding based on the location (town or country) and the amount
# by which the speed limit is exceeded. It also checks for camera detection and determines if the
# driver's license should be revoked.

# Constants for fine amounts
FINE_20_TO_40 = 500
FINE_40_TO_60 = 1000
FINE_60_TO_80 = 2000
FINE_OVER_80 = 5000

# Speed limits
TOWN_SPEED_LIMIT = 60
COUNTRY_SPEED_LIMIT = 90

# Vehicle speed, location, and camera detection
vehicle_speed = 200
is_in_town = True
is_camera_detected = False

# Initialize fine
fine = 0

# Calculate over speed
if is_in_town:
    over_speed = vehicle_speed - TOWN_SPEED_LIMIT
else:
    over_speed = vehicle_speed - COUNTRY_SPEED_LIMIT

# Determine the fine based on over speed
if over_speed < 20:
    print("Speed not exceeded or exceeded insignificantly")
elif 20 <= over_speed < 40:
    fine = FINE_20_TO_40
elif 40 <= over_speed < 60:
    fine = FINE_40_TO_60
elif 60 <= over_speed < 80:
    fine = FINE_60_TO_80
elif over_speed >= 80:
    fine = FINE_OVER_80

# Print the fine result
if fine > 0:
    print("Fine: " + str(fine))
else:
    print("Speed not exceeded or exceeded insignificantly")

# License revocation check
if fine >= 60 and not is_camera_detected:
    print("Driver's license revocation")
else:
    print("Speed exceeded, without driver's license revocation")
