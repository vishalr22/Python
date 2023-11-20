'''
update(): The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

Removing items from dictionary:
- clear(): The clear() method removes all the items from the list.
- pop(): The pop() method removes the key-value pair whose key is passed as a parameter.
- popitem(): The popitem() method removes the last key-value pair from the dictionary.
- del: we can also use the del keyword to remove a dictionary item.
If key is not provided, then the del keyword will delete the dictionary entirely.
'''

info = {'name': 'Vishal', 'age': 19, 'eligible': True}
print(info)
info.update({'age': 26})
info.update({'DOB': 1997})
print(info)

info.pop('eligible')
print(info)

info.popitem()
print(info)

del info['age']
print(info)

info.clear()
print(info)

info.update({'age': 26})
del info
# print(info)     # It will give error as the dictionary "info" is already deleted.