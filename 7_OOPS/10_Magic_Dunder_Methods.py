'''
Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes.
They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

Some of the most commonly used magic methods in Python:
1. __init__ method
The init method, also called "constructor" is a special method that is automatically invoked when you create a new instance of a class.

2. __str__ and __repr__ methods
The str and repr methods are both used to convert an object to a string representation.
The str method is used when you want to print out an object.
The repr method is used when you want to get a string representation of an object that can be used to recreate the object.

3. __len__ method
The len method is used to get the length of an object.

4. __call__ method
The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called.
It allows you to create objects that behave like functions.
'''


class Employee:
    def __init__(self, name) -> None:
        self.name = name

    def __len__(self):
        return sum(1 for _ in self.name)

    def __str__(self) -> str:
        return f"Object to string : {self.name}"

    def __repr__(self) -> str:
        return f"Name: {self.name}"

    def __call__(self):
        print("Function is getting called.")


e = Employee("Vishal")
print(e)  # is same as print(str(e))
print(repr(e))
print(e.name)
print(len(e))
e()
