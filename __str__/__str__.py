class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old."

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
 

class Juli(Person):
    def __init__(self):
        super().__init__("Juli", 29)

        if self.age == 26:
            print("True")
        else:
            print("False")




elvis = Person("Elvis", 54) 
jul = Juli()
both = (elvis, jul)
print(elvis, jul)
print(both)

