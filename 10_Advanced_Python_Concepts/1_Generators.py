'''
Generators in Python are special type of functions that allow you to create an iterable sequence of values. 
A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it.

Creating a Generator:
You can create a generator by using the 'yield' statement in a function. 
The 'yield' statement returns a value from the generator and suspends the execution of the function until the next value is requested.

next() function is used to request the next value from the generator, 
and the generator resumes its execution until it encounters another yield statement or until it reaches the end of the function.

Using a Generator:
Once you have created a generator, you can use it in a variety of ways, such as in a for loop, a list comprehension, or a generator expression.
'''


def my_generator():
    for i in range(5):
        yield i  # creating a generator


gen = my_generator()  # generator function my_generator() returns a generator object, which can be used to generate the values
print(next(gen))  # next() function request the next value from the generator
print(next(gen))
print(next(gen))

for i in gen:  # generator used in a for loop, just like any other iterable sequence. The generator is used to generate the values one-by-one as the loop iterates over it
    print(i)

'''
Benefits of Generators
Generators offer several benefits over other types of sequences, such as lists, tuples, and sets.
One of the main benefits of generators is that they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory.
This makes generators a powerful tool for working with large or complex data sets, as you can generate the values as you need them, rather than having to store them all in memory at once.

Another benefit of generators is that they are lazy, which means that the values are generated only when they are requested.
This allows you to generate the values in a more efficient and memory-friendly manner, as you don't have to generate all the values up front.
'''
