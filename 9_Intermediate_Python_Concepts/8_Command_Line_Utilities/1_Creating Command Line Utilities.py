'''
Command line utilities are programs that can be run from the terminal or command line interface.
In Python, you can create your own command line utilities using the built-in 'argparse' module.
'''
import argparse

parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("arg1", help="Username")
parser.add_argument("arg2", help="Password")

# Adding optional arguments
parser.add_argument("-o", "--optional", help="Software_Name", default=None)

# # Adding positional arguments
parser.add_argument("positional", help="URL of the software")

# # Adding arguments with type
parser.add_argument("-n", type=int, help="Status code")

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.arg1)
print(args.arg2)
print(args.optional)
print(args.positional)
print(args.n)


# Command to run while executing this file:
# python 1_Creating Command Line Utilities.py username password -o software_name https://www.ggogle.com -n 200
