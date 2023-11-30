'''
Shutil is a Python module that provides a higher level interface for working with file and directories. The name "shutil" is short for shell utility. 
It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories.

Some of the most commonly used functions in the shutil module are:
1. shutil.copy(source, destination): This function copies the file located at source to a new location specified by destination. If the destination location already exists, the original file will be overwritten.
2. shutil.copy2(source, destination): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.
3. shutil.copytree(source, destination): This function recursively copies the directory located at source to a new location specified by destination. If the destination location already exists, the original directory will be merged with it.
4. shutil.move(source, destination): This function moves the file located at source to a new location specified by destination. This function is equivalent to renaming a file in most cases.
5. shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell
'''

import shutil

# Copying a file
shutil.copy("source.txt", "destination.txt")

# Copying a directory
shutil.copytree("source_dir", "destination_dir")

# Moving a file
shutil.move("source.txt", "destination.txt")

# Deleting a directory
shutil.rmtree("directory")
