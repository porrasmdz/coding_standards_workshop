"""Module providin the solution for Coding Standards Workshop"""

from enum import IntEnum

class GradeThreshold(IntEnum):
    """Minimum average required for each letter grade."""
    A = 90
    B = 80
    C = 70
    D = 60

class Student:
    """Class representing a student and its utilities in this workshop program"""
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        """Add a valid grade to the student."""
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            raise TypeError("Grade must be numeric.")

        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")

        self.grades.append(grade)

    def calc_average(self):
        """Calculate average grade for this student instance and returns it"""
        if not self.grades or len(self.grades) < 1:
            raise ValueError("Student has no grades.")

        total = 0
        for grade in self.grades:
            total += grade
        avg = total / len(self.grades)
        return avg

    def check_honor(self):
        """Checks if student has honourable grade and assign it"""
        self.honor = self.calc_average() > 90
        return self.honor

    def get_letter(self):
        """Determine the letter grade based on the average."""
        average = self.calc_average()

        if average >= GradeThreshold.A:
            return "A"
        if average >= GradeThreshold.B:
            return "B"
        if average >= GradeThreshold.C:
            return "C"
        if average >= GradeThreshold.D:
            return "D"

        return "F"

    def delete_grade(self, index: int):
        """Remove a grade by its index."""

        if index < 0 or index >= len(self.grades):
            raise IndexError("Grade index is out of range.")

        del self.grades[index]

    def report(self):
        """Generates user report"""
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Final Grade: {self.get_letter()}")


if __name__ == "__main__":
    student = Student("x", "")

    try:
        student.add_grade(100)
        student.add_grade("Fifty")  # TypeError
    except (TypeError, ValueError) as error:
        print(f"Error adding grade: {error}")

    try:
        student.calc_average()
        student.check_honor()
    except ValueError as error:
        print(f"Error calculating grades: {error}")

    try:
        student.delete_grade(5)  # IndexError
    except (IndexError, TypeError) as error:
        print(f"Error deleting grade: {error}")

    try:
        student.report()
    except (ValueError, TypeError) as error:
        print(f"Error generating report: {error}")
