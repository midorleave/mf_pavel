from typing import List, Optional

class Student:
    def __init__(self, name: str, grades: Optional[List[int]] = None ):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)

elvi = Student("Elvis")
juldo = Student("Juldo", [77])
elvi.take_exam(86)

print(elvi.grades)
print(juldo.grades)
