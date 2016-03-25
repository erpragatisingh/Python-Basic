print(""" Siring Demo




""")

var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])



print("\n updateing string ")


var1 = 'Hello World!'

print ("Updated String :- ", var1[:6] + 'Python')


print(""" Escape Characters

\a	0x07	Bell or alert
\b	0x08	Backspace
 

\n	0x0a	Newline
\nnn	 	Octal notation, where n is in the range 0.7

\s	0x20	Space
\t	0x09	Tab
\v	0x0b	Vertical TabSpace

""")
print("""String Special Operators
Assume string variable a holds 'Hello' and variable b holds 'Python', then −""")


print("""String Special Operators
Assume string variable a holds 'Hello' and variable b holds 'Python', then −

Operator	Description	Example
+	Concatenation - Adds values on either side of the operator	a + b will give HelloPython
*	Repetition - Creates new strings, concatenating multiple copies of the same string	a*2 will give -HelloHello
[]	Slice - Gives the character from the given index	a[1] will give e
[ : ]	Range Slice - Gives the characters from the given range	a[1:4] will give ell
in	Membership - Returns true if a character exists in the given string	H in a will give 1
not in	Membership - Returns true if a character does not exist in the given string	M not in a will give 1
r/R	Raw String - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the
raw string operator,
the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark.
print r'\n' prints \n and print R'\n'prints \n""")


print("\n String Formatting Operator\n")


print ("My name is %s and weight is %d kg!" % ('Pragati', 21) )

print("\n Triple Quotes \n")



para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)
      

print("\n Unicode String \n")


print(u'Hello, world!')






