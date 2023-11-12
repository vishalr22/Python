'''
Variable is like a container that holds data. Creating a variable is like creating a placeholder in memory and assigning it some value.

Data type specifies the type of value a variable holds. In python, we can print the type of any operator using type function.

1. Numeric data: int, float, complex
int: 3, -8, 0
float: 7.349, -9.0, 0.0000001
complex: 6 + 2i

2. Text data: str
str: "Hello World!!!", "Python Programming"

3. Boolean data:
Boolean data consists of values True or False.

4. Sequenced data: list, tuple
list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. 
Lists are mutable and can be modified after creation.
Eg: list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]

Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. 
Tuples are immutable and can not be modified after creation.
Eg: tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))

5. Mapped data: dict
dict: A dictionary is an unordered collection of data containing a key:value pair. 
The key:value pairs are enclosed within curly brackets.
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
'''

a = 3
b = 3.3
c = complex(8, 2)
d = True
e = None
print("The type of a is ", type(a))
print("The type of b is ", type(b))
print("The type of c is ", type(c))
print("The type of d is ", type(d))
print("The type of e is ", type(e))

a1 = 9
print("Addition of", c, "and", a1, "is:", c+a1)

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name": "Vishal", "age": 20, "canVote": True}
print(dict1)