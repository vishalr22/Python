'''
Regular expressions, or "regex" is used for working with strings and text data in Python.
They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

Metacharacters in regular expressions:
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline.
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE to match.
()  Enclose a group of REs

Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions

In Python, regular expressions are supported by the 're' module.

re.search(pattern, text) - Searching for a pattern. re.search() method either returns None (if the pattern does not match),
or a re.MatchObject that contains information about the matching part of the string.
This method stops after the first match, so this is best suited for testing a regular expression more than extracting data.

re.findall(pattern, text) - used to find all occurrences of the pattern in a string and return in a list.

re.sub(pattern, substitute_text, text) - used to replace a pattern in a string.

re.finditer() - works exactly the same as the re.findall() method except it returns an iterator yielding match objects matching the regex pattern
in a string instead of a list.
'''

import re

pattern = r"[a-z]+at"  # Define a regular expression pattern
text = "The cat is in the hat."  # Match the pattern against a string

match = re.search(pattern, text)
if match:
    print("Match found!")
else:
    print("Match not found.")

matches = re.findall(pattern, text)
print(matches)

new_text = re.sub(pattern, "dog", text)
print(new_text)


print("!--------------Another Example----------------!")

# Extracting information from a string
text = "The email address is example@example.com."
pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)
print(match)
if match:
    email = match.group()
    print(email)

print("!--------------Another Example----------------!")

pattern = r"[A-z]+yclone"
text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. 
Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. It became a tropical disturbance on 2 March, 
and was named the next day after attaining tropical storm status. Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds 
of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg). As it tracked |
southeastwards, Dumazile weakened steadily over the next couple of days due to wind shear, and became a post-tropical cyclone on 7 March'''

matches = re.finditer(pattern, text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])  # This works same as match.group()
    # print(match.group())
