'''
Lambda function is a small anonymous function without a name.
lambda arguments: expression

Lambda functions can have multiple arguments, just like regular functions.
Lambda functions can also include multiple statements, but they are limited to a single expression.

Lambda functions are often used in situations where a small function is required for a short period of time.
They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.
'''

def apply(fx, value):
    return 6 + fx(value)

square = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(square(5))
print(cube(5))
print(avg(3, 5, 10))
print(apply(cube , 2))
