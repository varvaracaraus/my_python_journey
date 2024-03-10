# Student Information Aggregator
# This script processes a dictionary of student information, extracting and aggregating various data points:
# student ID and age pairs, a set of unique interests, and the total length of all surnames.

students = {
    1: {
        'name': 'Bob',
        'surname': 'Bertrand',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Fritz',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Gimello',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def get_student_info(student_dict: dict) -> tuple:
    """
    Aggregates information about students, including ID-age pairs, interests, and surname lengths.

    Args:
        student_dict (dict): A dictionary containing student information.

    Returns:
        tuple: Contains a list of tuples (ID, age), a set of interests, and total length of surnames.
    """
    # Creating ID-age pairs
    student_age_pairs = [(student_id, info['age']) for student_id, info in student_dict.items()]

    # Aggregating all unique interests
    all_interests = set(interest for info in student_dict.values() for interest in info['interests'])

    # Calculating the total length of all surnames
    total_surname_length = sum(len(info['surname']) for info in student_dict.values())

    return student_age_pairs, all_interests, total_surname_length


# Getting aggregated student information
pairs, interests, surname_length = get_student_info(students)

# Displaying the results
print("List of 'ID student — age' pairs:", pairs)
print("Full list of interests for all students:", interests)
print("Total length of all surnames:", surname_length)
