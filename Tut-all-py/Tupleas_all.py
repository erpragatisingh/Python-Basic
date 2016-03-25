 
print("""A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
The differences between tuples and lists are,
the tuples cannot be
changed unlike lists and tuples use parentheses, whereas lists use square brackets.

Creating a tuple is as simple as putting different comma-separated values. Optionally you can put these
comma-separated values between parentheses also. For example −""")



tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";


print("The empty tuple is written as two parentheses containing nothing −")
tup1 = (50,);
print(tup1)

print("\n Accessing Values in Tuples: \n")

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

print ("tup1[0]: ", tup1[0])
print( "tup2[1:5]: ", tup2[1:5])

print("\n Updating Tuples ")

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3)

# output 12, 34.56, 'abc', 'xyz')


print("Delete Tuple Elements")

tup = ('physics', 'chemistry', 1997, 2000);

print ("All tuples elements ",tup)
del tup;
print("Note an exception raised, this is because after del tup tuple does not exist any")

#print ("After deleting tup : ",tup)


print("Basic Tuples Operations")

print(len((1, 2, 3)))

print((1, 2, 3) + (4, 5, 6))

print(('Hi!',) * 4)

print(3 in (1, 2, 3))


for x in (1, 2, 3):
 print(x)


print("Indexing, Slicing, and Matrixes")

L = ('spam', 'Spam', 'SPAM!')
print("L[2] Offsets start at zero->",L[2])

print("Negative: count from the right ->",L[-2])

print("Slicing fetches sections- > " , L[1:])


print("No Enclosing Delimiters")


print ('abc', -4.24e93, 18+6.6j, 'xyz')
x, y = 1, 2;
print ("Value of x , y : ", x,y)


help (tuple)











