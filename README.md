# This Repo Covers Python from Basic to Advanced Level

# Python
- Python is a dynamically typed, general purpose programming language that supports an object-oriented programming approach as well as a functional programming approach.
- Python is an interpreted and a high-level programming language.
- It was created by Guido Van Rossum in 1989.

# Features of Python
- Python is simple and easy to understand.
- It is Interpreted and platform-independent which makes debugging very easy.
- Python is an open-source programming language.
- Python provides very big library support. Some of the popular libraries include NumPy, Tensorflow, Selenium, OpenCV, etc.
- It is possible to integrate other programming languages within python.

# What is Python used for?
- Python is used in Data Visualization to create plots and graphical representations.
- Python helps in Data Analytics to analyze and understand raw data for insights and trends.
- It is used in AI and Machine Learning to simulate human behavior and to learn from past data without hard coding.
- It is used to create web applications.
- It can be used to handle databases.
- It is used in business and accounting to perform complex mathematical operations along with quantitative and qualitative analysis.

# Modules in Python
Module is like a code library having the required packages related to that module by somebody else in our python program. There are two types of modules in python:
- Built in Modules - These modules are ready to import and use and ships with the python interpreter. There is no need to install such modules explicitly.
- External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.

# pip command
It can be used as a package manager pip to install a python module.
- pip/pip3 install <module_name>

Eg: <b>pip install pandas</b> or <b>pip3 install sklearn</b>

# import syntax
Import syntax is used to import a module in Python. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on. 
-  import <module_name>

Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation.
- import math <br> result = math.sqrt(9)

To import specific functions or variables from a module we use the from keyword. 
 - from math import sqrt <br> result = sqrt(9)

You can also import multiple functions or variables at once by separating them with a comma:
- from math import sqrt, pi

Importing everything: To import all functions and variables from a module we use the * wildcard.
- from math import *

Python also allows you to rename imported modules using the as keyword.
- import math as m <br> result = m.sqrt(9)

<b>dir</b> function: Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module.
- import math <br> print(dir(math))

# Python Comments
A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

- Single-Line Comments:  To write a comment just add a ‘#’ at the start of the line. Eg: <b># Comment Statement</b>
- Multi-Line Comments: To write multi-line comments you can use multiline string at each line or you can use the multiline string. Eg: <b>'''Comment Statement'''</b>

# Escape Sequence Characters
An escape sequence character is a backslash \ followed by the character you want to insert.

Eg: <b>print("This will print \n execute after new line")</b>

# PEP 8
PEP 8 is a document that provides guidelines and best practices on how to write Python code.
The primary focus of PEP 8 is to improve the readability and consistency of Python code.

PEP stands for Python Enhancement Proposal. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

Zen of Python - Guiding principles for Python’s design. 

- Command to check: <b>import this</b>