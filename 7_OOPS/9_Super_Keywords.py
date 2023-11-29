'''
super() keyword in Python is used to refer to the parent class.

When a class inherits from a parent class, it can override or extend the methods defined in the parent class.
However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.

It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.
'''


class ParentClass1:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def parentMethod(self):
        print(f"This is parent method 1: {self.name} having id {self.id}")


class ParentClass2:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def parentMethod(self):
        print(f"This is parent method 2: {self.name} having id {self.id}")


class ChildClass(ParentClass1, ParentClass2):
    def __init__(self, name, id, lang):
        super().__init__(name, id)  # It calls the parent_class_1_init using the super() keyword as ParentClass1 is the 1st class mentioned while inheriting.
        self.lang = lang

    def childMethod(self):
        print(f"This is child Method: {self.name} having id {self.id}")


p1 = ParentClass1('Ram', 1)
p2 = ParentClass2('Shyam', 2)
c1 = ChildClass('Ashish', 3, 'python')
c1.parentMethod()
c1.childMethod()
