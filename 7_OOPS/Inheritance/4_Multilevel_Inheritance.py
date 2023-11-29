'''
Multilevel inheritance is where a derived class inherits from another derived class.

Syntax:
class BaseClass:
    # Base class code

class DerivedClass1(BaseClass):
    # Derived class 1 code

class DerivedClass2(DerivedClass1):
    # Derived class 2 code
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"name: {self.name}")


class Dog(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show(self):
        Animal.show(self)
        print(f"color: {self.color}")


class Doggerman(Dog):
    def __init__(self, name, color, breed):
        Dog.__init__(self, name, color)
        self.breed = breed

    def show(self):
        Dog.show(self)
        print(f"breed: {self.breed}")


d1 = Doggerman('kutta', 'black', 'doggerman')
d1.show()
