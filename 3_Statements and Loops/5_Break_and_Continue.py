'''
break Statement: The break statement enables a program to skip over a part of the code.
A break statement terminates the very loop it lies within.

Continue Statement
The continue statement skips the rest of the loop statements and causes the next iteration to occur.
'''

for i in range(100):
    if i == 10:
        break
    else:
        print(i)


for i in [2, 3, 4, 5, 6]:
    if i % 2 != 0:
        continue
    else:
        print(i)