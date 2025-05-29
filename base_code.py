'''Initialize the class'''
class Student:
    '''Class represent a student with an id, name, grades to know whether it passed or no'''
    def __init__(self, identification, name):
        '''Initialize the class with an id and name'''
        if not identification or not name:
            raise ValueError("Name and ID must not be empty.")
        self.id = identification
        self.name = name
        self.grades = []
        self.passed = "NO"
        self.honor = "?"

    def add_grades(self, grade):
        '''This method enable to add a grade of a student'''
        if isinstance(grade, (int, float)):
            if 0 <= grade <= 100:
                self.grades.append(grade)
            else:
                print("Error: Grade must be between 0 and 100.")
        else:
            print("Error: Grade must be a numeric value.")

    def calcaverage(self):
        '''This method enable to calculate the average'''
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        '''Returns the letter grade based on the average'''
        avg = self.calcaverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def determine_pass_fail(self):
        '''Determines if the student passed or failed'''
        self.passed = "Passed" if self.calcaverage() >= 60 else "Failed"

    def check_honor(self):
        '''This method enable to check if the person have an honor certificate '''
        self.honor = "Yes" if self.calcaverage() >= 90 else "No"

    def delete_grade(self, value_or_index):
        '''This method enable to delete a grade'''
        if isinstance(value_or_index, int):
            if 0 <= value_or_index < len(self.grades):
                removed = self.grades.pop(value_or_index)
                print(f"Grade {removed} at index {value_or_index} removed.")
            else:
                print("Error: Index out of range.")
        else:
            try:
                value = float(value_or_index)
                if value in self.grades:
                    self.grades.remove(value)
                    print(f"Grade {value} removed.")
                else:
                    print("Error: Grade value not found.")
            except ValueError:
                print("Error: Invalid value to remove.")

    def report(self):  # broken format
        '''This method enable to show a report'''
        avg = self.calcaverage()
        self.determine_pass_fail()
        self.check_honor()
        letter = self.get_letter_grade()
        print("\n----- Student Summary Report -----")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade: {avg:.2f}")
        print(f"Letter Grade: {letter}")
        print(f"Pass/Fail: {self.passed}")
        print(f"Honor Roll: {self.honor}")
        print("----------------------------------")


def startrun():
    '''This method enable to start the program'''
    try:
        student = Student("12345", "Alice")
    except ValueError as e:
        print(f"Initialization Error: {e}")
        return

    # Valid and invalid grade inputs
    student.add_grades(95.0)
    student.add_grades(88.5)
    student.add_grades(102)       # Invalid
    student.add_grades(-10)       # Invalid
    student.add_grades("Fifty")   # Invalid

    # Removing grades
    student.delete_grade(1)      # Remove by index
    student.delete_grade(100.0)  # Invalid index
    student.delete_grade(95.0)   # Remove by value
    student.delete_grade("bad")  # Invalid value

    # Report
    student.report()


startrun()
