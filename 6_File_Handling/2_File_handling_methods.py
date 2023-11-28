# readline() method: reads a single line from the file.
f = open('myfile.txt', 'r')
line = f.readline()  # read the current line
print(line)
f.close()


# writelines() method writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)  # write the iterable object line by line in the file
f.close()


# readlines() method reads all the lines of the file and returns them as a list of strings.
f = open('myfile.txt', 'r')
output = f.readlines()  # read file line by line
print(output)
f.close()


# seek() function allows you to move the current position within a file to a specific point.
# The position is specified in bytes, and you can move either forward or backward from the current position.
with open('myfile.txt', 'r') as f:
    f.seek(10)  # Move to the 10th byte in the file
    data = f.read(5)  # Read the next 5 bytes
    print(data)
    f.close()


#  tell() function returns the current position within the file, in bytes.
with open('myfile.txt', 'r') as f:
    data = f.read(10)  # Read the first 10 bytes
    current_position = f.tell()  # Save the current position
    print(f.seek(current_position))  # Seek to the saved position
    f.close()


# truncate() function: to truncate the file to a specific size.
with open('myfile.txt', 'w') as f:
    f.write('Hello World!')
    f.truncate(5)  # truncate the file to a specific size,i.e, removes the remaining content

with open('myfile.txt', 'r') as f:
    print(f.read())
