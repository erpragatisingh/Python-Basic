print ("Python is really a great language,", "isn't it?")


str = input("Enter your input: ");
print ("Received input is : ", str)


str = input("Enter your input: ");
print ("Received input is : ", str)


print("Opening and Closing Files")

# Open a file
fo = open("foo.rtf", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode --: ", fo.mode)



# Open a file
fo = open("foo.rtf", "wb")
print ("Name of the file: ", fo.name)

# Close opend file
fo.close()


print("Reading and Writing Files----------\n")
# Open a file
fo = open("foo.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()


# Open a file
fo = open("foo.txt", "r+")
str = fo.read(17);
print ("Read String is : ", str)
# Close opend file
fo.close()



#...................................

print("""File Positions
The tell() method tells you the current position within the file; in other words, the next read or write will occur at that many bytes from the beginning of the file.

The seek(offset[, from]) method changes the current file position. The offset argument indicates the number of bytes to be moved. The from argument specifies the reference position from where the bytes are to be moved.

If from is set to 0, it means use the beginning of the file as the reference position and 1 means use the current position as the reference position and if it is set to 2 then the end of the file would be taken as the reference position.

Example
Let us take a file foo.txt, which we created above.""")


# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print ("Read String is : ", str)

# Check current position
position = fo.tell();
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print ("Again read String is : ", str)
# Close opend file
fo.close()


print("""Renaming and Deleting Files

Python os module provides methods that help you perform file-processing operations, such as renaming and deleting files.

To use this module you need to import it first and then you can call any related functions.

"""")



import os

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

#!/usr/bin/python
import os

# Delete file test2.txt
os.remove("text2.txt")

      


