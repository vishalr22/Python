'''
Hybrid inheritance is a combination of multiple inheritance and single inheritance.
It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class,
and single inheritance is used to inherit the properties of the derived class into a sub-derived class.

Syntax:
class BaseClass:
    # attributes and methods

class Derived1(BaseClass):
    # attributes and methods

class Derived2(BaseClass):
    # attributes and methods

class Derived3(Derived1, Derived2):
    # attributes and methods
'''


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address

    def show_details(self):
        Human.show_details(self)
        print("Address:", self.address)


class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)


class Student(Person):
    def __init__(self, name, age, address, program):
        Person.__init__(self, name, age, address)
        self.program = program

    def show_details(self):
        Person.show_details(self)
        self.program.show_details()  # call show_details() method of Program class using self.program


program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)  # program object is assigned as a parameter tp Student class
student.show_details()
