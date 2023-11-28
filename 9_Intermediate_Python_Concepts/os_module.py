'''
os module in Python is a built-in library that provides functions for interacting with the operating system. 
It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, 
and running system commands.
'''

import os

# get current working directory
cwd = os.getcwd()
print(cwd)

# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)
print(contents)

# Close the file
os.close(f)

# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")

# Close the file
os.close(f)

# Get a list of the files in the current directory
files = os.listdir(".")
print(files)

# Create a new directory
os.mkdir("Oops") 

# Run the "dir" command and print the output
output = os.system("dir")
print(output)    # it returns the output of dir command with 0 status code which means process exited without error

# Run the "ipconfig" command and get the output as a file-like object
f = os.popen("ipconfig")

# Read the contents of the output
output = f.read()
print(output)

# Close the file-like object
f.close()