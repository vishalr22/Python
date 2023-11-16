'''
if-else statement:
if the expression evaluates "True" execute the block of code inside if statement. After execution return to the code out of the if……else block.
if the expression evaluates "False" execute the block of code inside else statement. After execution return to the code out of the if……else block.
'''

applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")


# elif statements
n = 0
if n < 0:
    print("Less than Zero")
elif n == 0:
    print("Zero")
else:
    print("Greater than Zero")


# Nested if statements
m = 18
if m > 0:
    if m > 15:
        print("Greater than 15")
    else:
        print("Less than 15")
else:
    print("Less or equal to than zero")