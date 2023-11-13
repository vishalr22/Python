'''
Strings: Anything that you enclose between single or double quotation marks is considered a string. 

Accessing Characters of a String
A string is essentially a sequence or array of textual data. We can access parts of string by using its index which starts from 0.

Slicing of String
The method of specifying the start and end index to specify a part of a string is called slicing.

Length of a String
Length of a string can be find using len() function.

Loop through a String:
Strings are arrays and arrays are iterable. Thus we can loop through strings.
'''

firstName = "Vishal"
lastName = "Rawat"
print(f"Hello {firstName} {lastName} ")
print(firstName + lastName) # String Concatenation

multi_str = """Hello,
My Name is Vishal Rawat.
I am a software Developer"""
print(multi_str)
print(len(multi_str)) # Length of a string

print(firstName[0] + lastName[0])

print(f"{firstName[:2]}-{lastName[:3]}") # String Slicing

alphabets = "ABCDEFGH"
for i in alphabets:
    print(i)