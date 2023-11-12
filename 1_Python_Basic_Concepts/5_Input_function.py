'''
Input function - User take Input in python by using input() function. 
This input function gives a return value as string/character hence we have to pass that into a variable.

variable=input()

But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

variable=int(input())
variable=float(input())
'''

var = input("Enter the number: ")
print(var, "type is :", type(var))

var1 = int(input('Enter the number :'))
print(var1, "type is :", type(var1))