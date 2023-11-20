'''
Dictionaries are ordered collection of data items. 
They store multiple items in a single variable. 
Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

I. Accessing single values: We can access dictionary single value by mentioning keys either in square brackets or by using get method.
II. Accessing values: We can print all the values in the dictionary using values() method.
III. Accessing keys: We can print all the keys in the dictionary using keys() method.
IV. Accessing key-value pairs: We can print all the key-value pairs in the dictionary using items() method.
'''

info = {'name': 'Vishal', 'age': 26, 'eligible': True}
print(info['name'])
print(info.get('eligible'))

print(info.values())
print(info.keys())
print(info.items())
