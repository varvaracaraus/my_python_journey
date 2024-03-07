# Josephus Problem Simulator
# This script simulates the Josephus problem where people in a circle are eliminated
# every nth count until only one person is left.

# User input for the total number of people and the elimination count
total_people = int(input('Number of people: '))
elimination_count = int(input('Count for elimination: '))
print(f'This means that every {elimination_count} person drops out.')

# Initialize the circle of people
people = list(range(1, total_people + 1))
index = 0

# Eliminate people in the circle until only one remains
for _ in range(total_people - 1):
    print('\nCurrent circle of people:', people)
    start = index % len(people)  # Start counting from the current index
    index = (start + elimination_count - 1) % len(people)  # Determine who to eliminate
    print('Start counting from number', people[start])
    print(f'Person number {people.pop(index)} is eliminated')

# Print the last person remaining
print('\nThe person left is number', people[0])
