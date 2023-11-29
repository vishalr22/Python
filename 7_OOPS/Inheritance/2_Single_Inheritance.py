'''
Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class.

Syntax:
class ParentClass:
    # class body

class ChildClass(ParentClass):
    # class body

Single Inheritance allows you to reuse code, extend it to fit your needs, and make it easier to manage complex systems.
'''


# parent class
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.id = employee_id

    def show(self):
        print(f"{self.name} is having employee id {self.id}")


# 1st child class
class Developer(Employee):
    def __init__(self, name, developer_type):
        Employee.__init__(self, name, employee_id='21')
        self.type = developer_type

    def show(self):
        print(f"{self.name} with employee id {self.id} know {self.type}")


# 2nd child class
class Programmer(Developer):
    def __init__(self, name, developer_type, coding_lang):
        Developer.__init__(self, name, developer_type)
        self.coding_lang = coding_lang

    def show(self):
        print(f"{self.name} with employee id {self.id} know {self.coding_lang} {self.type}")


e1 = Employee('Hari Priya', 20)
e1.show()
d1 = Developer('Vishal', 'coding')
d1.show()
p1 = Programmer('vishal', 'coding', 'python')
p1.show()

print(Developer.mro())  # Method Resolution Order (MRO) is the set of rules that construct the linearization