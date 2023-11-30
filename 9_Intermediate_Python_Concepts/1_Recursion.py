'''
Recursion is the process of defining something in terms of itself.
Python Recursive Function is a function where it call itself.
'''

print("!---------factorial----------!")


def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))


num = 7
print("Number: ", num)
print("Factorial: ", factorial(num))


print("!---------fibonacci----------!")


def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)


n = int(input("Enter the number: "))
for i in range(n):
    print(fibonacci(i), end=" ")
