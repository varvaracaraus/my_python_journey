# Safe Depth Calculator for Egg Laying
# This script calculates an approximate safe depth for egg-laying based on a given maximum allowable danger level.
# It iteratively adjusts the depth range to find a depth where the danger level is within the acceptable deviation.

def danger_level(depth: float) -> float:
    """
    Calculates the danger level at a given depth using a specific mathematical formula.

    :param depth: The depth at which to calculate the danger level.
    :return: The calculated danger level at the given depth.
    """
    return depth ** 3 - 3 * depth ** 2 - 12 * depth + 10


def safe_depth(allowed_deviation: float) -> float:
    """
    Determines the safe depth for egg laying based on the maximum allowable danger level deviation.

    :param allowed_deviation: The maximum deviation from the safe danger level.
    :return: The calculated safe depth.
    """
    min_depth = 0
    max_depth = 4
    depth_result = (min_depth + max_depth) / 2

    while abs(danger_level(depth_result)) >= allowed_deviation:
        if abs(danger_level(min_depth)) < abs(danger_level(max_depth)):
            max_depth = depth_result
        else:
            min_depth = depth_result
        depth_result = (min_depth + max_depth) / 2

    return depth_result


# User input for the maximum allowable danger level
max_deviation = float(input('Enter the maximum allowable danger level: '))

# Calculate and output the safe depth
result = safe_depth(max_deviation)
print('Approximate safe depth for egg laying:', round(result, 2), 'm')
