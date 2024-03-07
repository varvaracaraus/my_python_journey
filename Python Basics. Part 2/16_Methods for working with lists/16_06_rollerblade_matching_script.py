# Rollerblade Matching Script
# This script calculates the maximum number of people who can take rollerblades based on the available sizes.

# User input for the number of rollerblades
skates_count = int(input('Number of rollerblades: '))

# Initialize a list to store the sizes of rollerblades
skate_sizes = []
for i in range(skates_count):
    size = int(input(f'Size of rollerblade {i + 1}: '))
    skate_sizes.append(size)

# User input for the number of people
people_count = int(input('\nNumber of people: '))

# Initialize a list to store people's foot sizes
people_sizes = []
for i in range(people_count):
    size = int(input(f'Foot size of person {i + 1}: '))
    people_sizes.append(size)

# Matching people with rollerblades based on size
skates_taken = 0
for size in skate_sizes:
    if size in people_sizes:
        skates_taken += 1
        people_sizes.remove(size)  # Remove the matched size from the list

# Print the maximum number of people who can take rollerblades
print(f'Maximum number of people who can take rollerblades: {skates_taken}')
