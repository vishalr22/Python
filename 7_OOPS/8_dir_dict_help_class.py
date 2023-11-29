'''
dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object.
It is a useful tool for discovering what you can do with an object.

__dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection

help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

    def show(self):
        print(f" {self.name} {self.age} {self.version}")


p = Person("John", 30)
print(dir(p))
print(p.__dict__)
print(help(p))
print(help(Person))  # this is give same thing as print(help(p))
