'''
While loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

Else with While Loop
else statement with while loop does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.


Do-While loop in python
do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop.
It is also known as an exit-controlled loop.
do{
    loop body;
}while(condition);

'''

x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')

# Using a while Loop to emulate the Do-while loop in Python
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:  # condition not number > 0 is equivalent to number <= 0
        break

# Using a For Loop to emulate the Do-while loop in Python
i = 1
while True:
    print(2*i)
    i += 1
    if not i <= 10:
        break
