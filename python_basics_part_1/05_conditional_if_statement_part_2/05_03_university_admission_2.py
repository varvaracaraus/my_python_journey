# University Admission and Scholarship Eligibility Checker
# This script determines whether a student is enrolled in a university and eligible for a scholarship
# based on their place in the list of entrants and their grades.

# Minimum requirements
minimum_place = 10
minimum_grades = 290

# Input for the student's place and grades
entrant_place = int(input("Type in your place in the list of entrants: "))

if entrant_place <= minimum_place:
    entrant_grades = int(input("Type in your grades: "))
    if entrant_grades >= minimum_grades:
        print("Enrolled + scholarship")
    else:
        print("Enrolled - scholarship")
else:
    print("Not enrolled")
