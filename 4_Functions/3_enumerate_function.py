'''
The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) 
and get the index and value of each element in the sequence at the same time in the form of tuple.
'''
# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)


# Changing the start index (Loop over a list and print the index (starting at 1) and value of each element)
# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors, start=1):
    print(f'{index+1}: {color}')


# Without enumerate
index = 0
for color in colors:
    print(f'{index+1}: {color}')
    index += 1