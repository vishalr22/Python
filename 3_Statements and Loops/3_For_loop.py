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


'''
For loop with else
Python allows the else keyword to be used with the for loops. The else block appears after the body of the loop. 
The statements in the else block will be executed after all iterations are completed.
The program exits the loop only after the else block is executed.

Syntax: 
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block
'''

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of loop")
