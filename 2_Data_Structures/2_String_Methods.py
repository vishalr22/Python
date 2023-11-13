'''
Python provides a set of built-in methods that we can use to alter and modify the strings.

upper() : converts a string to upper case.
lower() : converts a string to lower case.
strip() : removes any white spaces before and after the string.
rstrip() : removes any trailing characters
replace() : replaces all occurrences of a string with another string.
split() : splits the given string at the specified instance and returns the separated strings as list items.
capitalize() : turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.
center() : aligns the string to the center as per the parameters given by the user. We can also provide padding character. It will fill the rest of the fill characters provided by the user.
count() : returns the number of times the given value has occurred within the given string.
endswith() : checks if the string ends with a given value. If yes then return True, else return False. We can even also check for a value in-between the string by providing start and end index positions.
find() : searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1. The major difference being find() and index() is that index() raises an exception if value is absent whereas find() does not.
index() : searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
isalnum() : returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
isalpha() : returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
islower() : returns True if all the characters in the string are lower case, else it returns False.
isprintable() : returns True if all the values within the given string are printable, if not, then return False.
isspace() : returns True only and only if the string contains white spaces, else returns False.
istitle() : returns True only if the first letter of each word of the string is capitalized, else it returns False.
isupper() : returns True if all the characters in the string are upper case, else it returns False.
startswith() : checks if the string starts with a given value. If yes then return True, else return False.
swapcase() : changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
title() : capitalizes each letter of the word within the string.
'''

random_string = " My Name is Vishal !!"
print(random_string.upper())
print(random_string.lower())
print(random_string.strip())
print(random_string.rstrip("!"))
print(random_string.replace(" !!", "."))
print(random_string.split(" "))
print("random_string".capitalize())
print(random_string.center(50, "."))
print(random_string.count('a'))
print(random_string.endswith('!'))
print(random_string.find('is'))
print(random_string.index("Vishal"))
print("randomstring90".isalnum())
print("randomstring".isalpha())
print("vishal rawat".islower())
print("VISHAL RAWAT".isupper())
print(random_string.isprintable())
print("   ".isspace())
print("Vishal".istitle())
print(random_string.startswith(" My"))
print(random_string.swapcase())
print(random_string.title())