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
        if not isinstance(user_id, str) or not user_id.strip():
            raise ValueError("Student ID cannot be empty.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")

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
        self.honor = self.calc_average() > GradeThreshold.A
        return self.honor


    def check_passed(self):
        """Determines if the student has passed."""
        self.is_passed = self.calc_average() >= GradeThreshold.D
        return self.is_passed


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

    def delete_grade_by_value(self, grade):
        """Remove the first occurrence of a grade by value."""
        if grade not in self.grades:
            raise ValueError(f"Grade {grade} does not exist.")

        self.grades.remove(grade)

    def report(self):
        """Generates user report"""
        average = self.calc_average()
        self.check_passed()
        self.check_honor()

        print("===== STUDENT REPORT =====")
        print(f"Student ID: {self.id}")
        print(f"Student Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {self.get_letter()}")
        print(f"Pass/Fail: {'Passed' if self.is_passed else 'Failed'}")
        print(f"Honor Roll: {self.honor}")


if __name__ == "__main__":
    print("\n===== 1. ADD STUDENTS =====")
    student = Student("001", "John Doe")
    print(f"Student created: {student.id} - {student.name}")

    print("\n===== 2. ADD GRADES =====")
    for lgrade in [95.0, 72.5, 88.0]:
        student.add_grade(lgrade)
        print(f"Grade added: {lgrade}")
    print(f"Current grades: {student.grades}")

    print("\n===== 3. CALCULATE AVERAGE =====")
    print(f"Average grade: {student.calc_average():.2f}")

    print("\n===== 4. DETERMINE LETTER GRADE =====")
    for lgrade in [95, 85, 75, 65, 55]:
        example = Student(f"TEST-{lgrade}", "Test Student")
        example.add_grade(lgrade)
        print(f"Average: {lgrade} -> Letter: {example.get_letter()}")

    print("\n===== 5. DETERMINE PASS/FAIL =====")
    for lgrade in [90, 60, 59]:
        example = Student(f"PASS-{lgrade}", "Test Student")
        example.add_grade(lgrade)
        example.check_passed()
        status = "Passed" if example.is_passed else "Failed"
        print(f"Average: {lgrade} -> {status}")

    print("\n===== 6. HANDLE INVALID INPUTS =====")

    for userid, username in [("", "John"), ("002", "")]:
        try:
            Student(userid, username)
        except (ValueError, TypeError) as error:
            print(f"Invalid student: {error}")

    for lgrade in ["Fifty", -10, 150]:
        try:
            student.add_grade(lgrade)
        except (ValueError, TypeError) as error:
            print(f"Invalid grade ({lgrade}): {error}")

    print("\n===== 7. HONOR ROLL DETECTION =====")
    for lgrade in [95, 90, 89]:
        example = Student(f"HONOR-{lgrade}", "Test Student")
        example.add_grade(lgrade)
        print(f"Average: {lgrade} -> Honor Roll: {example.check_honor()}")

    print("\n===== 8. REMOVE A GRADE =====")
    example = Student("003", "Jane Doe")

    for lgrade in [95.0, 80.0, 70.0]:
        example.add_grade(lgrade)

    print(f"Initial grades: {example.grades}")

    example.delete_grade(1)
    print(f"After removing index 1: {example.grades}")

    example.delete_grade_by_value(95.0)
    print(f"After removing value 95.0: {example.grades}")

    try:
        example.delete_grade(10)
    except (IndexError, TypeError) as error:
        print(f"Invalid index: {error}")

    try:
        example.delete_grade_by_value(100.0)
    except ValueError as error:
        print(f"Invalid value: {error}")

    print("\n===== 9. STUDENT SUMMARY REPORT =====")
    student.report()
