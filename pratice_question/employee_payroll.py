"""
Q4. Employee Payroll
 Create FullTimeEmployee, Contractor, and Intern, each with different pay calculations. A Payroll class should compute the total monthly cost without using if isinstance(...).

Tests: polymorphism, abstract base classes (abc)
Twist: add a Manager who earns a bonus based on their reports. Does Payroll need to change? how i thinking to slove this so how i able to slove this question ?
"""

"""
thinking in this question --

fulltimeemployee is a Employee --> yes (inheritance)
Payroll has a Employee --> Yes (composition)

Step 1: Find the “same action, different behavior”

    Ask: What do all employees do that works differently?

    Answer: they all get paid, but the calculation is different.

    Employee	How pay is calculated
    FullTimeEmployee	Fixed monthly salary
    Contractor	hourly rate × hours worked
    Intern	Fixed stipend

    Same action (monthly_pay()), different behavior = polymorphism.

Step 2: Find the “rule everyone must follow”

    Ask: What must every employee class have?

    Answer: a monthly_pay() method. So we make an abstract class Employee with an abstract monthly_pay(). That is abstraction.

Step 3: Make Payroll “dumb” on purpose

    Payroll should not know what kind of employee it has. It just says: “Every employee has monthly_pay(). Let me call it and add up.”

    That’s why no if isinstance(...) is needed.

"""


from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def monthly_pay(self):
        pass

    @abstractmethod
    def display(self): 
        pass

class FullTimeEmployee(Employee):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def monthly_pay(self):
        return self.salary

    def display(self):
        print(f"Full-Time | {self.name} | Pay: ₹{self.monthly_pay()}")


class Contractor(Employee):

    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def monthly_pay(self):
        return  self.hourly_rate *  self.hours

    def display(self):
        print(f"Contractor | {self.name} | {self.hours} hrs x ₹{self.hourly_rate} = ₹{self.monthly_pay()}")
    

class Intern(Employee):

    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def monthly_pay(self):
        return self.stipend

    def display(self):
        print(f"Intern | {self.name} | Stipend: ₹{self.monthly_pay()}")



class PayRoll:

    def __init__(self):
        self.employees = []

    def add(self, employees):
        self.employees.append(employees)

    def total_cost(self):
        total = 0

        for e in self.employees:
            total = total + e.monthly_pay()

        return total

    def display_all(self):
        for e in self.employees:
            e.display()                
        print(f"Total Monthly Cost: ₹{self.total_cost()}")
    

harish = FullTimeEmployee("Harsih", 50000)
jayesh = Contractor("Jayesh", 500, 80)
mandar = Intern("Mandar", 10000)

p = PayRoll()
p.add(harish)
p.add(jayesh)
p.add(mandar)

p.display_all()