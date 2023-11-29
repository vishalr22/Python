'''
A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function.
The new function is often referred to as a "decorated" function.

Python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code.
They are used for a variety of purposes, such as logging, memoization, access control, and more.

@decorator_function
def my_function():
    pass
'''


def greet(fx):
    def mfx(*args):
        print("Good Morning")
        fx(*args)
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    print("Hello world")


@greet
def add(a, b):
    print(a+b)


# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)


# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.
def log_function_call(func):
    def decorated(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
    return decorated


@log_function_call
def my_function(a, b, c=4):
    return a + b + c


my_function(5, 6)
