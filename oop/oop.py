class Student: 
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grades(self):
        return sum(self.grades) / len(self.grades)

student = Student("Elvis", (88, 99, 78, 100, 51))
student2 = Student("Bob", (96, 78, 44, 86, 100))

print(student.name, student.average_grades())
#print(student.average_grades())
print(student2.name, student2.average_grades())
#print(student2.average_grades())
 