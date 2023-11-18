'''
Tuples
Tuples are ordered collection of data items. They store multiple items in a single variable. 
Tuple items are separated by commas and enclosed within round brackets (). 
Tuples are unchangeable meaning we can not alter them after creation.

Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. 
The first item has index [0], second item has index [1], third item has index [2] and so on.

Range of Index: You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.
Syntax: Tuple[start : end : jumpIndex]
'''

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)
print(details[0])   # positive indexing
print(details[-1])  # negative indexing

if 18 in details:
    print('18 in details.')
else:
    print('18 is not in details.')

print(details[0:3:2])