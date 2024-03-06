# Math Grade Response
# This script asks for a student's math grade and provides a response based on the grade. 
# Grades of 2 or 3 result in a prompt to study more, while grades of 4 or 5 are praised.

# Input for the math grade
math_grade = int(input('What did you get in math? '))

# Provide a response based on the grade
if math_grade == 2 or math_grade == 3:
    print('Not good. Go and study!')
elif math_grade == 4 or math_grade == 5:
    print('Good job! You can relax.')
