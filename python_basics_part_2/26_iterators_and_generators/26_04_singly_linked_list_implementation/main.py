from linked_list import LinkedList

# Create an instance of LinkedList
my_list = LinkedList()

# Append data to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Display the current list
print('Current list:', my_list)

# Access and display the third element
print('Getting the third element:', my_list.get(2))

# Remove the second element
print('Removing the second element.')
my_list.remove(1)

# Display the list after removal
print('New list:', my_list)
