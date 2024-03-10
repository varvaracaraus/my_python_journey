# List Combination and Counting
# This script combines lists 'a' and 'b', then removes all occurrences of the number 5.
# It then combines the resulting list with list 'c' and counts the occurrences of the number 3.

# Initial lists
a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

# Combining list 'a' with list 'b'
a.extend(b)
print('Number of digits 5 when first combined:', a.count(5))

# Removing all occurrences of 5
while 5 in a:
    a.remove(5)

# Combining the updated list 'a' with list 'c'
a.extend(c)
print('Number of digits 3 in the second combination:', a.count(3))
print('Final list:', a)
