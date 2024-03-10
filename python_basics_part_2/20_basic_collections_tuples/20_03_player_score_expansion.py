# Player Score Expansion
# This script expands a dictionary of players' names and their scores into a list of tuples,
# where each player's first name, last name, and individual scores are separate elements.

# Dictionary of players with their scores
players = {
    ("Loic", "Louis"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# Expanding the dictionary into a list of tuples
result = [(name[0], name[1], *scores) for name, scores in players.items()]

# Displaying the result
print(result)
