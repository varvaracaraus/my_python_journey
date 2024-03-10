# Container Weight Position Finder
# This script determines the position of a new container by its weight compared to existing containers.
# Containers must have a weight between 0 and 200.

# Reading the number of existing containers
quantity = int(input('Number of containers: '))

# List to store the weights of containers
containers = []

# Collecting weights of existing containers
for _ in range(quantity):
    while True:
        weight = int(input('Enter container weight: '))
        if 0 <= weight <= 200:
            containers.append(weight)
            break
        else:
            print('The weight of the container must be in the range from 0 to 200.')

# Collecting weight of the new container
while True:
    new_container = int(input('Enter the weight of the new container: '))
    if 0 <= new_container <= 200:
        break
    else:
        print('The weight of the container must be in the range from 0 to 200.')

# Determining the position for the new container
position = 1
for container in containers:
    if new_container <= container:
        position += 1

# Displaying the position of the new container
print(f'The number the new container will receive is: {position}')
