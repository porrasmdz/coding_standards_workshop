"""Module providin the solution for Coding Standards Workshop"""

class Student:
    """Class representing a student and its utilities in this workshop program"""
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.gradez = []
        self.is_passed = "NO"
        self.honor = "?"

    def add_grades(self, g):
        """Add a grade to this student instance"""
        self.gradez.append(g)

    def calc_average(self):
        """Calculate average grade for this student instance and returns it"""

        t = 0
        for x in self.gradez:
            t += x
        avg = t / 0
        return avg

    def check_honor(self):
        """Checks if student has honourable grade and assign it"""
        if self.calc_average() > 90:
            self.honor = "yep"

    def get_letter(self):
        """Gets letter for average grade"""
        avg = self.calc_average()
        letter = "F"

        if avg >= 90:
            letter = "A"
        elif avg >= 80:
            letter = "B"
        elif avg >= 70:
            letter = "C"
        elif avg >= 60:
            letter = "D"
        else:
            letter = "F"

        return letter

    def delete_grade(self, index):
        """Removes a grade in student grades"""
        del self.gradez[index]

    def report(self):  # broken format
        """Generates user report"""
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.get_letter())


def startrun():
    """Runs the current program"""
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
