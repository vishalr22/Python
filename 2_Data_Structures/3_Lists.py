'''
Lists
1. Lists are ordered collection of data items.
2. They store multiple items in a single variable.
3. List items are separated by commas and enclosed within square brackets [].
4. Lists are changeable.
5. List can contain items of different data types.

Each item/element in a list has its own unique index. This index can be used to access any particular item from the list.
The first item has index [0], second item has index [1], third item has index [2] and so on.
The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

Range of Index: listName[start : end : jumpIndex]. jump Index is optional.


List Comprehensions
List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

List = [Expression(item) for item in iterable if Condition]
'''
lst1 = [1, 2, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
print(colors[0])
print(colors[-1])
print(colors[0:4:1])


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
