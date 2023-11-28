'''
A local variable is a variable that is defined within a function and is only accessible within that function. 
It is created when the function is called and is destroyed when the function returns.

On the other hand, a global variable is a variable that is defined outside of a function and is accessible 
from within any function in your code.

Global Keyword
The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope.
Global keyword is also used to modify a global variable from within a function. (Not recommended to change global variable generally)
'''

x = 10  # global variable
print(f"Global Variable value before changing: {x}")


def my_function():
    global x
    x = 5  # this will change the value of the global variable x
    y = 5  # local variable


my_function()
print(f"Global Variable value after changing: {x}")  # prints 5
# print(y)  # this will cause an error because y is a local variable and is not accessible outside of the function.
