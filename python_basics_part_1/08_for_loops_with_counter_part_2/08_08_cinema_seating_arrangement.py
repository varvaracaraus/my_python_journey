# Cinema Seating Arrangement
# This script arranges a group of boys and girls in a cinema in such a way that no more than two boys or girls 
# sit next to each other. The script outputs the seating arrangement or indicates if a solution isn't possible.

# Input for the number of boys and girls
number_of_boys = int(input("Enter the number of boys: "))
number_of_girls = int(input("Enter the number of girls: "))

# Initialize the result string
seating_arrangement = ''

# Determine the seating arrangement
if (number_of_boys > number_of_girls * 2) or (number_of_girls > number_of_boys * 2):
    print('No solution.')
elif number_of_boys >= number_of_girls:
    difference = number_of_boys - number_of_girls
    for _ in range(difference):
        seating_arrangement += "BGB"
    for _ in range(number_of_girls - difference):
        seating_arrangement += "BG"
else:
    difference = number_of_girls - number_of_boys
    for _ in range(difference):
        seating_arrangement += "GBG"
    for _ in range(number_of_boys - difference):
        seating_arrangement += "GB"

# Print the seating arrangement
print(seating_arrangement)
