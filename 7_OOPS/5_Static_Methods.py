'''
Static methods are methods that belong to a class rather than an instance of the class.
They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self).
The method can be called on the class itself, without the need to create an instance (object) of the class.
Static methods are often used to create utility functions that don't need access to instance data.
'''


class Math:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b


result = Math.add(1, 2)
print(result)

a = Math(5)
a.add_to_num(6)
print(a.num)

print(a.add(5, 2))  # static method called using object
print(Math.add(7, 2))  # static method called using class
