"""
create student class that takes name and makrts of 3 subject as arguments in constructor
then create a method to print the average marks of the student.
"""

class Student:

    def __init__(self, name , mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    @staticmethod
    def hello():
        print("hello")

    def average(self):
        avg = (self.mark1 + self.mark2 + self.mark3) / 3
        print(f"Average marks of {self.name} is: {avg}")

s1 = Student("John", 85, 90, 78)
s1.hello()
s1.average()

