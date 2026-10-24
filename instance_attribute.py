"""
Instance Attribute
Instance attribute - Its a unique information which is specific to that object is called instance attribute.

so we can create instance attribute by using self keyword.
example :

__init__ method - its a constructor method which is used to initialize the instance attribute.
self - its a reference variable which is used to refer current object.

example:

class Student:
    collage_name = "ABC College" # this is a class attribute

    def __init__(self, name, age, roll_number):
        self.name = name  # this is a instance attribute
        self.age = age  # this is a instance attribute
        self.roll_number = roll_number  # this is a instance attribute


s1 = Student("John", 20, 101)
s2 = Student("Alice", 21, 102)

print(s1.collage_name, s1.name, s1.age, s1.roll_number)
print(s2.collage_name, s2.name, s2.age, s2.roll_number)
"""


class Student:
    collage_name = "ABC College" # this is a class attribute

    def __init__(self, name, age, roll_number):
        self.name = name  # this is a instance attribute
        self.age = age  # this is a instance attribute
        self.roll_number = roll_number  # this is a instance attribute


s1 = Student("John", 20, 101)
s2 = Student("Alice", 21, 102)

print(s1.collage_name, s1.name, s1.age, s1.roll_number)
print(s2.collage_name, s2.name, s2.age, s2.roll_number)