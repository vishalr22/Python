'''
if "__name__ == "__main__" in Python
In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module.
When a Python script is run directly, the __name__ variable is set to the __main__
When the script is imported as a module into another script, the __name__ variable is set to the name of the module.
'''
# script.py
def main():
    print("Running script directly from this same script")

print(__name__)

if __name__ == "__main__":
    main()

'''
This is useful if you have code that you want to reuse in multiple scripts,
but you only want it to run when the script is run directly and not when it's imported as a module.
'''
# # This is another script: script2.py
# import script
# print(__name__)   # Here if we run this script then "print(__name__) will print "script2"
# script.main()     # It will call the main function from script.py
