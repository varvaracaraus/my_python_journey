# Container Weight Positioning
# This script determines the position where a new container should be placed based on its weight
# in comparison to the existing containers. All containers must have a weight between 0 and 200.

# Get the number of existing containers
quantity = int(input('Number of containers: '))

# Initialize a list to store the weights of the containers
containers = []

# Input the weights of existing containers and validate the input
for _ in range(quantity):
    while True:
        weight = int(input('Enter container weight: '))
        if 0 <= weight <= 200:
            containers.append(weight)
            break
        else:
            print('The weight of the container must be in the range from 0 to 200.')

# Input and validate the weight of the new container
while True:
    new_container = int(input('Enter the weight of the new container: '))
    if 0 <= new_container <= 200:
        break
    else:
        print('The weight of the container must be in the range from 0 to 200.')

# Determine the position of the new container
position = 1
for container in containers:
    if new_container <= container:
        position += 1

# Print the determined position
print(f'The number the new container will receive is: {position}')
