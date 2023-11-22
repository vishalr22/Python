# In python, we can raise custom errors by using the 'raise' keyword.
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")


a = input("Enter the number between 5 and 9: ")
if a != "quit" and not 5 < int(a) < 9:
    raise ValueError("Not a valid input")


# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.
'''
class CustomError(Exception):
    # code ...
try:
    # code ...
except CustomError:
    # code...
'''
# This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.