'''
When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. 
In addition, it can have its own properties and methods, this is called as inheritance.

Syntax:
class BaseClass:
    Body of base class
class DerivedClass(BaseClass):
    Body of derived class
    
Types of inheritance:
1. Single inheritance
2. Multiple inheritance
3. Multilevel inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
'''


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id 

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def __init__(self, name, id, language):
        Employee.__init__(self, name, id)
        self.language = language

    def showLanguage(self):
        print(f"The default langauge is {self.language}")


e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer('Vishal', 200, 'Python')
e2.showDetails()
e2.showLanguage()
