'''
Access specifiers/modifiers are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

Types of access modifiers
1. Public access modifier
2. Private access modifier
3. Protected access modifier
'''


# Public Access Modifier in Python
class Student:
    '''
    All the variables and methods (member functions) in python are by default public.
    Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
    '''
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable


obj = Student(21, "HariPriya")
print(obj.age)
print(obj.name)
print(obj.__doc__)


# Private Access Modifier
class Student:
    '''
    Private members of a class (variables or methods) are those members which are only accessible inside the class.
    We cannot use private members outside of class.

    A variable or method should be considered private by prefixing its name with a double underscore (__)
    '''
    def __init__(self, age, name):
        self.__age = age      # private variable
        # self.__funName()    # can be declared like this

    def __funName(self):  # private function
        self.y = 34
        return self.y


class Subject(Student):
    pass


obj = Student(21, "Vivek")
obj1 = Subject

# # calling by object of class Student
# print(obj.__age) # gives error
# print(obj.__funName()) # gives error

# # calling by object  of class Subject
# print(obj1.__age) # gives error
# print(obj1.__funName()) # gives error

#  Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.
print(obj._Student__age)
print(obj._Student__funName())

'''
Name mangling: It is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses.
Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.
'''


# Protected Access Modifier
class Student:
    '''
    Protected method or attribute of a class that is intended to be accessed only by the class itself and its subclasses.
    The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.

    It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member.
    '''
    def __init__(self):
        self._name = "Vishal"

    def _funName(self):      # protected method
        return "Coding"


class Subject(Student):       # inherited class
    pass


obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
