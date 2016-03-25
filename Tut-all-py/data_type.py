print("\n Standard Data Types \n")


print("""Python has five standard data types −

Numbers

String

List

Tuple

Dictionary
""")


print("""var1 = 1
var2 = 10 You can also delete the reference to a
number object by using the del statement.
The syntax of the del statement is −""")




var1 = 1
var2 = 10


print("var 1", var1)
print("var 2", var2)


del var1


print("var 2", var2)
# print("var 1" ,var1)


print("Here are some examples of numbers − \n\n")

print("""int	long	float	complex
10	51924361L	0.0	3.14j
100	-0x19323L	15.20	45.j
-786	0122L	-21.9	9.322e-36j
080	0xDEFABCECBDAECBFBAEl	32.3+e18	.876j
-0490	535633629843L	-90.	-.6545+0J
-0x260	-052318172735L	-32.54e100	3e+26J
0x69	-4721885298529L	70.2-E12	4.53e-7j
Python allows you to use a lowercase L
with long, but it is recommended that you use only an uppercase L to
avoid confusion with the number 1. Python displays long integers with
an uppercase L.

A complex number consists of an ordered pair of real
floating-point numbers denoted by x + yj, where x and y are the real numbers
and j is the imaginary unit.\n """)



print("\n Python Strings \n")

print("""Strings in Python are identified as a contiguous set of characters represented in the quotation marks.
Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the
slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way
from -1 at the end.

The plus (+) sign is the string concatenation operator and
the asterisk (*) is the repetition operator. For example −""")


str = 'Hello World!'

print (str )         # Prints complete string
print (str[0] )      # Prints first character of the string
print (str[2:5] )    # Prints characters starting from 3rd to 5th
print (str[2:] )     # Prints string starting from 3rd character
print (str * 2 )     # Prints string two times
print (str + "TEST") # Prints concatenated string













