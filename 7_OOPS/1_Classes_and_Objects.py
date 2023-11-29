'''
A class is a blueprint or a template for creating objects. It defines the properties and methods that an object of that class will have. 
Properties are the data or state of an object, and methods are the actions or behaviors that an object can perform. 
They are created using the class keyword.

Object is the instance of the class used to access the properties of the class.

Constructors:
__init__() is known as constructor in OOP. It is a class special method used to create and initialize an object of a class.
A constructor is a unique function that gets called automatically when an object is created of a class.
The main purpose of a constructor is to initialize or assign values to the data members of that class. 
It cannot return any value other than None.

Parameterized Constructor: When the constructor accepts arguments along with self, it is known as parameterized constructor.
Syntax: def __init__(self, animal, group):

Default Constructor: When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.
Syntax: def __init__(self):
'''


# class creation
class Person:

    def __init__(self, name, occ, net_worth):  # parameterized constructor
        self.name = name
        self.occupation = occ
        self.net_worth = net_worth

    # self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person("Vishal", "S/W developer", 14)  # object creation
b = Person("hari", "S/W Engineer", 16)

a.info()  # method call
b.info()

a.name = "Shubham"  # property/variable change action
a.occupation = "Accountant"

a.info()  # method call
