class Student:
    """A class to represent a student with a full name, group number, and grades."""

    def __init__(self, full_name: str, group_number: int, grades: list[int]):
        """
        Initialize the student with full name, group number, and list of grades.
        """
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

    def calculate_average_grade(self) -> float:
        """Calculate and return the average grade of the student."""
        return sum(self.grades) / len(self.grades)
