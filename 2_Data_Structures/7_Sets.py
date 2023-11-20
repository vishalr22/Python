'''
Sets are unordered collection of data items. 
They store multiple items in a single variable. 
Set items are separated by commas and enclosed within curly brackets {}. 
Sets are unchangeable, meaning you cannot change items of the set once created.
Sets do not contain duplicate items.
Sets cannot be accessed using index numbers.
'''

info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)

# To create an empty set. Check using the type() function whether the type of the variable is a set.
set_list = set()
print(type(set_list))