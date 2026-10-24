"""
abstraction - This module contains the abstract base classes for the different components of the system

Hiding the implementation details and showing only functionality to the user is known as abstraction.

why in this display function is abstract - Because we want to ensure that all subclasses of Student must implement their own version of the display method, but the base class doesn't provide a concrete implementation.
"""
from abc import ABC, abstractmethod

class Student(ABC):
    collage_name = "ABC College" # this is a class attribute

    def __init__(self, name, age, roll_number):
        self.name = name  # this is a instance attribute
        self.age = age  # this is a instance attribute
        self.roll_number = roll_number  # this is a instance attribute

    @abstractmethod
    def display(self):
        pass

class StudentDetails(Student):
    def display(self):
        print(self.collage_name, self.name, self.age, self.roll_number)

class StudentMarks(Student):
    def __init__(self, name, age, roll_number, mark1, mark2, mark3):
        super().__init__(name, age, roll_number)
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def display(self):
        avg = (self.mark1 + self.mark2 + self.mark3) / 3
        print(f"Average marks of {self.name} is: {avg}")

s1 = StudentDetails("John", 20, 101)
s1.display()
s2 = StudentMarks("Alice", 21, 102, 85, 90, 78)
s2.display()