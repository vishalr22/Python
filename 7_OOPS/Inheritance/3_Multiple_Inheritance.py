'''
Multiple inheritance allows a class to inherit attributes and methods from multiple parent classes.
This can be useful in situations where a class needs to inherit functionality from multiple sources.

Syntax:
class ParentClass1:
    # class body

class ParentClass2:
    # class body

class ChildClass(ParentClass1, ParentClass2):
    # class body

Multiple inheritance follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes.
The MRO determines the order in which parent classes are searched for attributes and methods.
'''


class Dad:
    def __init__(self, dad_name, dad_work):
        self.dad_name = dad_name
        self.dad_work = dad_work

    def dad_details(self):
        print(f"Dad's name is {self.dad_name} and he is a {self.dad_work}")


class Mom:
    def __init__(self, mom_name, mom_work):
        self.mom_name = mom_name
        self.mom_work = mom_work

    def mom_details(self):
        print(f"Mom's name is {self.mom_name} and she is a {self.mom_work}")


class Child(Mom, Dad):
    def __init__(self, child_name, child_work):
        Mom.__init__(self, mom_name="Bina", mom_work="house_wife")
        Dad.__init__(self, dad_name="Bindeshwari", dad_work="Manager")
        self.child_name = child_name
        self.child_work = child_work

    def child_details(self):
        print(f"Child's name is {self.child_name} and he is a {self.child_work}. \
{self.child_name} father's name is {self.dad_name} and his mom name is {self.mom_name}")


son = Child('Vishal','Software developer')
son.child_details()
son.mom_details()
son.dad_details()

print("----------------------------------------------------")


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        print(f"Sound made by the animal {self.species}")


class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color


class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed

    def make_sound(self):
        print("Bark!")


d = Dog('kutta', "Doggerman", 'black')
d.make_sound()
a = Animal("billi", 'cat')
a.sound()
d.sound()
