from child import Child
from parent import Parent

# Program to simulate a parent-child relationship
# The Parent class can add, feed, and comfort children.
# The Child class maintains the state of each child.

parent_info = input("Enter the name and age of the parent, separated by a comma: ")
parent_name, parent_age = parent_info.split(", ")
parent = Parent(parent_name, int(parent_age))

num_children = int(input("Enter the number of children: "))

for _ in range(num_children):
    child_info = input(f"Enter the name, age, hungry or full, and upset or calm for the child, separated by a comma: ")
    name, age, mood_hungry, mood_upset = child_info.split(", ")
    child = Child(name, int(age), mood_hungry, mood_upset)
    parent.add_child(child)

for child in parent.children:
    if child.mood_hungry == "hungry":
        parent.feed_child(child)
    if child.mood_upset == "upset":
        parent.comfort_child(child)

for child in parent.children:
    child.info()
