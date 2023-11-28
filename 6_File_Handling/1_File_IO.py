'''
Opening a File: Python provides the open() function to open a file. 
It takes two arguments: the name of the file and the mode in which the file should be opened.

Modes in file
1. read (r): This mode opens the file for reading only and gives an error if the file does not exist. 
This is the default mode if no mode is passed as a parameter.

2. write (w): This mode opens the file for writing only and creates a new file if the file does not exist. 
Keep in mind that writing to a file will overwrite its contents if file already exists and contain contents.

3. append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

4. create (x): This mode creates a file and gives an error if the file already exists.

5. text (t): t refers to the text mode. t mode is used to handle text files.
There is no difference between r and rt or w and wt since text mode is the default. 
The default mode is 'r' (open for reading text, synonym of 'rt' ).

6. binary (b): used to handle binary files (images, pdfs, etc).
'''

f = open('myfile.txt', 'r')  # open file in read mode
contents = f.read()  # read a file
print(contents)

f = open('myfile.txt', 'w')  # open file in write mode
f.write('Hello, world!')  # write in file

f = open('myfile.txt', 'a')  # open file in append mode
f.write('\nHello, Vishal!')

# Closing the file is important because it releases the resources used by the file and allows other programs to access it.
f.close()  # close the file

# with statement can be used to automatically close the file after you are done with it.
with open('myfile.txt', 'r') as f:
    contents = f.read()
    print(contents)
    # ... do something with the file
