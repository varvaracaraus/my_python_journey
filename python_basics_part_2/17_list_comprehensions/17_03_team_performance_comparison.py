# Team Performance Comparison
# This script compares the performance scores of two teams, generating random scores between 5 and 10.
# It then determines the winners of each round based on higher scores.

import random

# Generating random scores for each team member
first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

# Displaying the scores of both teams
print('First team:', first_team)
print('Second team:', second_team)

# Determining the winners for each round
winners = [max(first_team[i], second_team[i]) for i in range(len(first_team))]

# Displaying the winners
print('Winners of the round:', winners)
