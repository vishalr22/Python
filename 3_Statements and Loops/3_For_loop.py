'''
for loops can iterate over a sequence of iterable objects in python. 
Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

range(): if we want to use for loop for a specific number of times then we use range() function.
range(start,stop,step)

'''

name = 'Vishal'
for i in name:
    print(i, end=", ")

colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)

for i in range(1, 15, 2):
    print(i)