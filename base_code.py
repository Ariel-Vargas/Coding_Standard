'''Initialize the class'''
class Student:
    '''Class represent a student with an id, name, grades to know whether it passed or no'''
    def __init__(self, ident, name):
        '''Initialize the class with an id and name'''
        self.id = ident
        self.name = name
        self.grades = []
        self.passed = "NO"
        self.honor = "?"

    def add_grades(self, grade):
        '''This method enable to add a grade of a student'''
        if isinstance(grade, (int, float)):
            self.grades.append(grade)

    def calcaverage(self):
        '''This method enable to calculate the average'''
        t = 0
        for x in self.grades:
            t += x

    def check_honor(self):
        '''This method enable to check if the person have an honor certificate '''
        if self.calcaverage() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        '''This method enable to delete a grade'''
        del self.grades[index]

    def report(self):  # broken format
        '''This method enable to show a report'''
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.grades))
        print("Final Grade = " + self.calcaverage())


def startrun():
    '''This method enable to start the program'''
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calcaverage()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
