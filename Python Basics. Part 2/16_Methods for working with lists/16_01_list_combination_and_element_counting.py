# List Combination and Element Counting
# This script combines lists and counts the occurrences of specific elements after each combination.
# It also removes specific elements from the combined list before the next combination.

# Initial lists
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

# Extend list 'a' with elements from list 'b'
a.extend(b)

# Count and print the number of digits '5' after the first combination
print('Number of digits 5 when first combined:', a.count(5))

# Remove all instances of digit '5' from list 'a'
while 5 in a:
    a.remove(5)

# Extend list 'a' with elements from list 'c'
a.extend(c)

# Count and print the number of digits '3' after the second combination
print('Number of digits 3 in the second combination:', a.count(3))

# Print the final combined list
print('Final list:', a)
