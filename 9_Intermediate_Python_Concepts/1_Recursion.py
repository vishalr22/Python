'''
Recursion is the process of defining something in terms of itself.
Python Recursive Function is a function where it call itself.
'''


def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))

num = 7
print("Number: ",num)
print("Factorial: ",factorial(num))