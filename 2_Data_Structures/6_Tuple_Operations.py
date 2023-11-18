'''
Manipulating Tuples
Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. 
Then perform operation on that list and convert it back to tuple.

However, we can directly concatenate two tuples without converting them to list.
'''

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       # add item
temp.pop(3)                 # remove item
temp[2] = "Finland"         # change item
countries = tuple(temp)
print(countries)


countries = ("Pakistan", "Afghanistan", "Bangladesh", "SriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


'''
Tuple Methods
tuple.count(element) - returns the number of times the given element appears in the tuple.
tuple.index(element, start, end) - returns the first occurrence of the given element from the tuple.    
Note: tuple.index(element) method raises a ValueError if the element is not found in the tuple.
'''

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)


Tuple2 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple2.index(3)
print('First occurrence of 3 is', res)