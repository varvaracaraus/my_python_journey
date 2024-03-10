# Space Food Consumption Tracker
# This script simulates the monthly consumption of food in space, starting with 100kg.
# Every month, 4kg of food is consumed. The script prints the remaining food supply each month.

# Initialize the number of months
months = 0

# Loop for food consumption
for remaining_food in range(100, 0, -4):
    months += 1
    print(f'In {months} month(s): {remaining_food} kg left.')
