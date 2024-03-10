# Academic Performance Assessment in a Class
# This script asks for the number of students and then their individual grades. It then evaluates 
# which grade (excellent, good, or average) is the most common in the class.

# Input for the number of students
number_of_students = int(input('Enter the number of students: '))

# Initialize counters for each grade
excellent_students = 0
good_students = 0
average_students = 0

# Collect and count grades for each student
for student in range(1, number_of_students + 1):
    grade = int(input(f'Enter the grade of student {student}: '))
    if grade == 5:
        excellent_students += 1
    elif grade == 4:
        good_students += 1
    elif grade == 3:
        average_students += 1

# Evaluate and print the most common grade category
if excellent_students > good_students and excellent_students > average_students:
    print('Today there are more excellent students.')
elif good_students > excellent_students and good_students > average_students:
    print('Today there are more good students.')
else:
    print('Today there are more average students.')
