# University Admission
# This script calculates the total score from English, Math, and Computer Science exams
# and determines if the applicant is eligible for a scholarship.

# Input for exam scores
english_score = int(input('Enter your English language score: '))
math_score = int(input('Enter your math score: '))
computer_science_score = int(input('Enter your computer science score: '))
passing_score = 270

# Check if the total score meets the scholarship criteria
total_score = english_score + math_score + computer_science_score
if total_score >= passing_score:
    print('Congratulations, you were admitted with a scholarship!')
else:
    print('Unfortunately, you were admitted without a scholarship!')
