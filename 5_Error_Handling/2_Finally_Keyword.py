'''
When we handle exception using the try and except block, we can include a finally block at the end. 
The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources 
or closing database connection or may be ending the program execution with a delightful message.

try:
    # statements which could generate 
    # exception
except:
    # solution of generated exception
finally:
    # block of code which is going to execute in any situation
'''

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")


def func1():
    try:
        list1 = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(list1[i])
        return 1
    except Exception as e:
        print("Some error occurred: ", e)
        return 0
    finally:
        print("I am always executed")
    print("I am always executed")


func_name = func1()
print(func_name)
