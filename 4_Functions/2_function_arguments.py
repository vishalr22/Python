# Function Arguments and return statement
'''
1. Default arguments: We can provide a default value while creating a function. 
This way the function assumes a default value even if a value is not provided in the function call for that argument.
'''
def details(fname, sname='rawat', age=26):
    print(f"Hello {fname} {sname} {age}")

details('vishal')



'''
2. Keyword arguments: We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. 
Hence, the the order in which the arguments are passed does not matter.
'''
def name_details(fname, sname, age):
    print(f"Hello {fname} {sname} {age}")

name_details(sname='rawat', fname='vivek', age=26)



'''
3. Required arguments: In case we don't pass the arguments with a key = value syntax, then it is necessary to pass the arguments in 
the correct positional order and the number of arguments passed should match with actual function definition.
'''
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")




'''
Variable-length arguments
1. Arbitrary Arguments: While creating a function, pass a * before the parameter name while defining the function. 
    The function accesses the arguments by processing them in the form of tuple.
2. Keyword Arbitrary Arguments: While creating a function, pass a ** before the parameter name while defining the function. 
    The function accesses the arguments by processing them in the form of dictionary.
'''
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("S", "Hari", "Priya")


def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname="Buchanan", lname="Quill", fname="James")


def variableLength(*args, **dict_new):
    print("hello", dict_new['name'], "from", dict_new['place'])
    print(f"This is {args[0]} {args[1]} ")

variableLength('hari', 'priya', name = 'vishal',place = 'bangalore')


'''
return Statement: The return statement is used to return the value of the expression back to the calling function.
'''
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))