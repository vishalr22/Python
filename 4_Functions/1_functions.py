'''
A function is a block of code that performs a specific task whenever it is called. 
In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

Built-in functions: These functions are defined and pre-coded in python.
min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

User-defined functions: We can create functions to perform specific tasks as per our needs.

Syntax:
def function_name(parameters):
    # Code and Statements

Calling a function: We call a function by giving the function name, followed by parameters (if any) in the parenthesis.
'''

name = "vishalrawat"
print(len(name))


def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")


num = int(input("Enter the number: "))
table(num)