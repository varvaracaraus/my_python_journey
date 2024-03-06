# Earth Volume Comparison
# This script calculates the volume of a planet based on the user-provided radius and compares
# it to the volume of Earth. It then prints how many times greater or smaller the volume of Earth
# is compared to the user-specified planet.

import math

# Earth's volume in cubic kilometers (approximate)
earth_volume = 10.8321 * 10 ** 11

# Input for the radius of a random planet
random_radius = float(input('Enter the radius of a random planet in kilometers: '))

# Calculate the volume of the random planet
random_planet_volume = (4 / 3) * math.pi * random_radius ** 3

# Compare the volumes and print the result
if earth_volume > random_planet_volume:
    print(f'The volume of the Earth is {round(earth_volume / random_planet_volume, 3)} times greater.')
elif earth_volume < random_planet_volume:
    ratio = random_planet_volume / earth_volume
    print(f'The volume of the Earth is {round(ratio, 3)} times smaller (1/{round(1/ratio, 3)}).')
