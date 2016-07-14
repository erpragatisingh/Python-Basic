print ("Opening and Closing files")

# Open a file

fo = open("foo.rtf", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode --: ", fo.mode)


# Close a file

fo.close()
print ("Closed or not: ", fo.closed)


print ("Reading and writing files.....\n")

# Open a file
fo = open("foo.txt", "w")
fo.write("Python is a great language.\n yeah its great!! \n");

# Open a file

fo.close()


# Open a file
fo = open("foo.txt", "rt")
str = fo.read(17);
print ("Read string is : ", str)

# Close a file
fo.close()
