##Regular Expression::

## how to define he pattern:
## a, X, 9 <-- ordinary characters just match themselves exactly.
## the meta characters which do not match hemselves because they have special meanings are:
## . ^ $ * + ? { [ ] \ | ( ) (datails below)

## . (a period) -- matches any single character except newline '\n'

## \w -- (lowecase w) matches a 'word' character: a lette or a digit or underbar [a-z A-Z 0-9].

## Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word.

## \W -- (uppercase w) matches any non-word character.

##re.search
##re.ndall
##re.compile
##re.sub

###########################re.search#####################################

print("\n1:")

import re
str = 'an example word:cat!!'
##match = re.search(r'word:\w\w\w', str)
match1 = re.search(r'word:\w\w\w', str)

## if statement after search() tests if it succeeded?

if match1:
    print('found', match1.group()) ## 'found word:cat'
    print('found', match1)

else:
    print('did not find')
############################re.search####################################

print("\n2:")

def Find(x,y):
    res = re.search(x,y)
    if res:
        print (res.group())
    else:
        print ("not found")

y = "shalini.16gla@gmail.com"

Find(r'\w@\w\w\w\w\w.\w\w\w',y)


############################re.search####################################

print("\n3:")

def Find(x,y):
    #res = re.search(x,y,re.M)
    res = re.search(x,y,re.I|re.M)
    if res:
        print (res.group())
    else:
        print ("not found")

y = "ashalini.16gla@gmail.com"
z = "shalini.16gla@gmail.com"
w = """xnaaccsa
cdscxscscscsc
ascscscscscs"""
u = "Ashalini.16gla@gmail.com"

Find("^a",y)
Find("^s",z)
Find("^a",z)
Find("^a",w)
Find("^a",u)


###############################re.search#################################

print("\n4:")

import re

line = "cats are smarter than dogs"

searchObj = re.search(r'(.*)are(.*?).*',line,re.M|re.I)

if searchObj:
    print ("searchObj.group():",searchObj.group())
    print ("searchObj.group(1):",searchObj.group(1))
    print ("searchObj.group(2):",searchObj.group(2))
else:
    print ("Nothing found!!")
    
##########################re.match######################################

print("\n5:")

import re

line = "cats are smarter than dogs"

matchObj = re.match(r'(.*)are(.*?).*',line,re.M|re.I)

if matchObj:
    print ("matchObj.group():",matchObj.group())
    print ("matchObj.group(1):",matchObj.group(1))
    print ("matchObj.group(2):",matchObj.group(2))
else:
    print ("No match!!")


###########################re.sub#####################################

print("\n6:")

import re

phone = "2004-959-559 # this is phone number"

# delete python-style comments
num = re.sub(r'#.*$', "",phone)
print ("Phone Num:", num)

# remove everything other than digits
num = re.sub(r'\D', "",phone)
print ("Phone Num:", num)


###########################re.search#####################################

print("\n7:")

import re

text = "blablablubb@gmail.com"
result = re.search("blablubb@gmail.com",text)

if result:
    print ("email address found:",result.group())
else:
    print ("email address not found")


###########################re.search#####################################

print("\n8:")

import re

text = "blablablubb@gmail.com"
result = re.search(".@......",text)

if result:
    print ("email address found:",result.group())
else:
    print ("email address not found")
