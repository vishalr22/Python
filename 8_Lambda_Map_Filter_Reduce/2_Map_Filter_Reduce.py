'''
The map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. 
These functions are known as higher-order functions, as they take other functions as arguments.
'''


'''The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.'''
# Syntax: map(function, iterable)

numbers = [1, 2, 3, 4, 5]  # List of numbers
doubled = map(lambda x: x * 2, numbers)  # Double each number using the map function
print(list(doubled))  # Print the doubled numbers


'''The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and 
# returns a new sequence containing only the elements that meet the predicate.'''
# Syntax: filter(predicate, iterable)

numbers = [1, 2, 3, 4, 5]  # List of numbers
evens = filter(lambda x: x % 2 == 0, numbers)  # Get only the even numbers using the filter function
print(list(evens))  # Print the even numbers



'''The reduce function is a higher-order function that applies a function to a sequence and returns a single value.'''
# Syntax: reduce(function, iterable)
# The function argument is a function that takes in two arguments and returns a single value.

from functools import reduce
numbers = [1, 2, 3, 4, 5]  # List of numbers
sum = reduce(lambda x, y: x + y, numbers)  # Calculate the sum of the numbers using the reduce function
print(sum)  # Print the sum

# The reduce function applies the function to the first two elements in the iterable and then applies the
# function to the result and the next element, and so on. The reduce function returns the final result.