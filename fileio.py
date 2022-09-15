
# Reading an existing file with read() function
f = open("file1.txt")
content = f.read(5)
print("Content of file: ", content)
content = f.read(5)
print("Content of file: ", content)
f.close()


# Reading an existing file with readlines() function
f = open("file1.txt")
content = f.readlines()
print("Content of file: ", content)
f.close()


# Writing a new file
f = open("file2.txt", "w")
content = "This is a demo file. It contains only the demo text for demonstration purpose. "
f.write(content)
print("Content added in file2.txt")
f.close()
f = open("file2.txt", "r")


# Appending an existing file
f = open("file3.txt", "a")
content = "This file is another demo file. This contains some text for demonstration purpose for showing the append in a file. Each time this program will execute, new content will get added into the file. "
f.write(content)
print("Content appended in file3.txt")
f.close()


# A new method of reading a file
with open("file1.txt") as f:
    a = f.read()
    print("==== Content of file1.txt ====\n", a)
