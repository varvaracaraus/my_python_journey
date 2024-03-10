# Rollerblade Size Matcher
# This script matches rollerblade sizes with people's foot sizes to determine the maximum number of people who
# can take rollerblades.

# Reading the number of rollerblades available
skates_count = int(input('Number of rollerblades: '))
skate_sizes = []

# Collecting rollerblade sizes
for i in range(skates_count):
    size = int(input(f'Size of rollerblade {i + 1}: '))
    skate_sizes.append(size)

# Reading the number of people and their foot sizes
people_count = int(input('\nNumber of people: '))
people_sizes = []

for i in range(people_count):
    size = int(input(f'Foot size of person {i + 1}: '))
    people_sizes.append(size)

# Determining the maximum number of people who can take rollerblades
skates_taken = 0
for size in skate_sizes:
    if size in people_sizes:
        skates_taken += 1
        people_sizes.remove(size)

# Displaying the result
print(f'Maximum number of people who can take rollerblades: {skates_taken}')
