'''
The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. 
This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.
'''

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())


names = ["John", "Jane", "Jim"]
if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")


foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
print(foods)

# It is important to note that the Walrus Operator should be used sparingly as it can make code less readable if overused.
