'''
Method overriding allows you to redefine a method in a derived class.
The method in the derived class is said to override the method in the base class.
When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.

It's important to note that when you override a method, the new implementation must have the same method signature as the original method.
This means that the number and type of arguments, as well as the return type, must be the same.
'''


class Shape:
    def __init__(self, size):
        self.size = size

    def area(self):
        return self.size * self.size


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(size=radius)  # __init__ method overriding using super keyword
        self.radius = radius

    def area(self):  # area method overriding
        return 3.14 * (super().area())


c = Circle(5)
print(c.area())

'''
By using method overriding, you can create more robust and reliable code, and ensure that your classes behave in the way that you need them to.
Additionally, by using the super function, you can extend the behavior of a base class method, rather than replace it, giving you even greater flexibility and control over the behavior of your classes.
'''
