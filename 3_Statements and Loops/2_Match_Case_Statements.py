'''
A match statement will compare a given variable value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.
match variable_name:
    case ‘pattern1’ : //statement 1
    case ‘pattern2’ : //statement 2
    …            
    case ‘pattern n’ : //statement n
'''

x = 4
match x:
    case 0:
        print("x is 0")
    case 4 if x % 2 == 0:
        print("x is 4")
    case _ if x < 10:
        print("x is less than 10")
    case _:
        print("x")