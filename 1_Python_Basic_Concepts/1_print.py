'''
print statement can be used to print something on the console in python

Syntax: print(object(s), sep=separator, end=end, file=file, flush=flush)
1. object(s): Any object, and as many as you like. Will be converted to string before printed
2. sep='separator': Specify how to separate the objects, if there is more than one. Default is ''
3. end='end': Specify what to print at the end. Default is '\n' (line feed)
4. file: An object with a write method. Default is sys.stdout
'''

print("Hello World!")
print(5, end=" ")
print(5*5)
print("Vishal\nRawat")
print("Python", "Java", 7)
print("My name is ", " Vishal", sep='-')