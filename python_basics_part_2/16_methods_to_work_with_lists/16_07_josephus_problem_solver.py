# Josephus Problem Solver
# This script simulates the Josephus problem, eliminating every nth person in a circle until only one remains.

# Reading the number of people and the elimination count
total_people = int(input('Number of people: '))
elimination_count = int(input('Count for elimination: '))
print(f'This means that every {elimination_count} person drops out.')

# Creating a list of people
people = list(range(1, total_people + 1))
index = 0

# Eliminating people until one is left
for _ in range(total_people - 1):
    print('\nCurrent circle of people:', people)
    start = index % len(people)
    index = (start + elimination_count - 1) % len(people)
    print('Start counting from number', people[start])
    print(f'Person number {people.pop(index)} is eliminated')

# Displaying the last person left
print('\nThe person left is number', people[0])
