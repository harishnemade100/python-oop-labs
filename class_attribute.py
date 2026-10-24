"""
class - its a blue print.
object - its a instance of a class.

example:

imagine collage have multiple student and each student have different attributes like name, age, roll number, etc.
so we can create a class called student and then we can create multiple objects of that class with different attributes.


class Attribute - Its Common infroamtion which is shared by all the objects of that class is called class attribute.

example:

class Student:
    college_name = ""ABC College"" # this is a class attribute


s1.Student()
s2.Student()
"""


class Student:
    college_name = "ABC College"  # this is a class attribute


s1 = Student()
s2 = Student()

print(s1.college_name)
print(s2.college_name)


""""
class attribute - Its not necessary a contant value, you can change its value
"""
Student.college_name = "XYZ College"
print("udpate", s1.college_name)
print("udpate", s2.college_name)



"""
if you want change for speficic object then you can change it by using object name.
"""
s1.college_name = "PQR College"
print("s1", s1.college_name)
print("s2", s2.college_name)