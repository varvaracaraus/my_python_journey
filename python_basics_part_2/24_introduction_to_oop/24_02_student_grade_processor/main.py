from student import Student


def get_average_grade(a_student: Student) -> float:
    """
    Return the average grade of a student.
    :param a_student: Student object
    :return: Average grade of the student
    """
    return a_student.calculate_average_grade()


def read_students_from_file(path: str) -> list[Student]:
    """
    Read student information from a file and return a list of Student objects.
    :param path: File path to read students from
    :return: List of Student objects
    """
    students_read = []
    with open(path, 'r') as file:
        for line in file:
            full_name, group_number, *grades = line.strip().split(', ')
            individual_student = Student(full_name, int(group_number), list(map(int, grades)))
            students_read.append(individual_student)
    return students_read


# Main execution logic
file_path = 'students.txt'
students_list = read_students_from_file(file_path)

sorted_students = sorted(students_list, key=get_average_grade)

for each_student in sorted_students:
    print(f'{each_student.full_name}: Average - {each_student.calculate_average_grade()}')
