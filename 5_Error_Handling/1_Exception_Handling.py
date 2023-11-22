'''
Exception handling is the process of responding to unwanted or unexpected events when a program runs to avoid the program or system crashing,
and without this process, exceptions would disrupt the normal operation of a program.

Exceptions in Python
Python has many built-in exceptions that are raised when your program encounters an error.
When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled.
If not handled, the program will crash.

Python try...except
try….. except blocks are used in python to handle errors and exceptions.
The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

try:
    # statements which could generate
    # exception
except:
    # Solution of generated exception
'''

a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

# Enter the number other than int to see the exception
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(f"Error is: {e}")


# We can also handle different types of error such as ValueError, IndexError or MemoryError
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError as e:
    print("Value Error :", e)
except IndexError as i:
    print("Index Error: ", i)
except MemoryError as m:
    print("Memory error:", m)
