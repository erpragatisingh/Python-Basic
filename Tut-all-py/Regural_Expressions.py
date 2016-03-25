print("""


A regular expression is a special sequence of characters that helps you
match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.

The module re provides full support for Perl-like regular expressions
in Python. The re module raises the exception re.error if an error occurs
while compiling or using a regular expression.

We would cover two important functions, which would be used to handle
regular expressions. But a small thing first: There are various characters,
which would have special meaning when they are used in regular expression.
To avoid any confusion while dealing with regular expressions,
we would use Raw Strings as r'expression'.


""")


import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


print("The search Function\n")

import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")


print("\n\n\n  Matching Versus Searching \n\n\n")


import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!" )     


print("\n\n Search and Replace \n\n")

import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)



print("""

Anchors
This needs to specify match position.

Example	Description
^Python	Match "Python" at the start of a string or internal line

Python$	Match "Python" at the end of a string or line

\APython	Match "Python" at the start of a string

Python\Z	Match "Python" at the end of a string

\bPython\b	Match "Python" at a word boundary

\brub\B	\B is nonword boundary: match "rub" in "rube" and "ruby" but not alone

Python(?=!)	Match "Python", if followed by an exclamation point.

Python(?!!)	Match "Python", if not followed by an exclamation point.



""")



print("""


Special Syntax with Parentheses
Example	Description
R(?#comment)	Matches "R". All the rest is a comment

R(?i)uby	Case-insensitive while matching "uby"

R(?i:uby)	Same as above

rub(?:y|le))	Group only without creating \1 backreference



""")


   
