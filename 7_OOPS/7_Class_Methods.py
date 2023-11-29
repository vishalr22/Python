'''
Class method is a type of method that is bound to the class and not the instance of the class.
In other words, it operates on the class as a whole, rather than on a specific instance of the class.
Class methods are defined using the "@classmethod" decorator, followed by a function definition.
The first argument of the function is always "cls," which represents the class itself.

Example:
class ExampleClass:
    @classmethod
    def factory_method(cls, argument1, argument2):
        return cls(argument1, argument2)


Note: Class methods cannot modify the class in any way. If you need to modify the class, you should use a class level variable instead.
'''


class Employee:
    company = 'Apple'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Employee name: {self.name}, age: {self.age}, {self.company} company {Employee.company}")

    @classmethod
    def company(cls, new_company):
        cls.company = new_company


emp1 = Employee('Vishal', 26)
emp1.show_details()
emp1.company('Tesla')
emp1.company = 'Tesla'
emp1.show_details()


'''
Class Methods as Alternative Constructors
There are times when you may want to create an object in a different way, or with different initial values, than what is provided by the default constructor.
This is where class methods can be used as alternative constructors.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))


person = Person.from_string("John Doe, 30")
print(person.name, person.age)
