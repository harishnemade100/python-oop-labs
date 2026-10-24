"""
Methods - Functions defined inside a class are called methods.
"""

class Student:
    collage_name = "ABC College" # this is a class attribute

    def __init__(self, name, age, roll_number):
        self.name = name  # this is a instance attribute
        self.age = age  # this is a instance attribute
        self.roll_number = roll_number  # this is a instance attribute

    def display(self):
        print(self.collage_name, self.name, self.age, self.roll_number)


s1 = Student("John", 20, 101)
s1.display()