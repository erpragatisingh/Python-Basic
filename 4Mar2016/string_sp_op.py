# String Special Operators

a="Hello"
b='Python'

# +	Concatenation - Adds values on either side of the operator
print  a + b # will give HelloPython
#  *	Repetition - Creates new strings, concatenating multiple copies of the same string
print a*2 # will give -HelloHello
# []	Slice - Gives the character from the given index
print a[1] # will give e
#  [ : ]	Range Slice - Gives the characters from the given range
print a[1:4] # will give ell
# in	Membership - Returns true if a character exists in the given string
# print H in a # will give 1
print(H in a)

#not in	Membership - Returns true if a character does not exist in the given string
#print M not in a #will give 1
print M not in a
# r/R	Raw String - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark.
# print r'\n' prints \n and print R'\n'prints \n
# %	Format - Performs String formatting	See at next section

print "My name is %s and weight is %d kg!" % ('Zara', 21) 
