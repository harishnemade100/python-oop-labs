"""
Encapsulation - its keep data safe inside the class, and let others use it only through controlled methods.

example of encapsulation in python:

in student class we have three instance attributes name, age and roll_number. 
if we want to keep these attributes safe then we can make them private by using double underscore(__) before the attribute name.
"""

class Student:
    collage_name = "ABC College" # this is a class attribute

    def __init__(self, name, age, roll_number):
        self.__name = name  # this is a instance attribute
        self.__age = age  # this is a instance attribute
        self.__roll_number = roll_number  # this is a instance attribute

    def display(self):
        print(self.collage_name, self.__name, self.__age, self.__roll_number)


s1 = Student("John", 20, 101)
s1.display()
