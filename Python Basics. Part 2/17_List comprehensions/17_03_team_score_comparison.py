import random

# Team Score Comparison
# This script generates random scores for two teams and compares them to determine the winner in each round.

# Generate scores for two teams using random numbers
first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]

# Print the scores of the first and second teams
print('First team:', first_team)
print('Second team:', second_team)

# Determine winners for each round based on the higher score
winners = [max(first_team[i], second_team[i]) for i in range(len(first_team))]

# Print the winners of each round
print('Winners of the round:', winners)
