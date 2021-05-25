class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}.")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}.")
    
    @staticmethod
    def static_method():
        print("Called static_method.")

ClassTest.class_method()
ClassTest.static_method()

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"Book {self.name} is {self.book_type} of weight {self.weight}g."

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight)

book = Book.hardcover("Culture map", 950)
light = Book.paperback("Art War", 600)

print(book, light)