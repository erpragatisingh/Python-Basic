def times(x, y):                #create and assign a function
    return (x*y)                #Body executed when called


a=times(2, 4)                   #Arguments in paranthese
print(a)

b=times('NI',5)                  #Functions are "typeless"
print(b)


def intersect(seq1, seq2):
    res = []                        #start empty
    for x in seq1:                  #scan seq1
        if x in seq2:               #Common item?
            res.append(x)           #Add common item to end

    return res


s1 = "SPAM"
s2 = "SCAM"
out = intersect(s1, s2)
print (out)


print ("\nRequired Argumnets : \n")

#function definition is here 
def req_arg(str,int):
    print("input a string and an integer")
    print(str*int)
    return

#function call is here
#req_arg(,)
#req_arg("Hi All ",)
#req_arg(,3)
req_arg("Hi All ",3)



print("=================================================")    
print ("\nKeyword Argumnets : \n")

#function definition is here
def req_arg(str,int):
    print("input a string and an integer")
    print(str*int)
    return

#function call is here
req_arg(int = 6, str = "Hi All ")

print("=================================================")
print ("\nDefault Argumnets : \n")

#function definition is here
def req_arg(str = "i m shalini ",int = 2):
    print("input a string and an integer")
    print(str*int)
    return

#function call is here
req_arg("hello",)
req_arg("hello",3)
req_arg()


print("=================================================")
print ("\nVariale-length Argumnets : \n")

#function definition is here 
def req_arg(str = "#",*vartuple):
    print("input a string and an integer")
    print(str)
    for x in vartuple:
        print (x)
    return

#function call is here
req_arg()               #dafault arguments
req_arg("hello",3)      #keyword arguments
req_arg("&",2,3)


print("=================================================")
print ("\nVariale-length Argumnets : \n")

#function definition is here 
def req_arg(str = "#",*vartuple):
    print("input a string and an integer")
    print(str)
    for x in vartuple:
        #print (x)
        print (str*x)
    return

#function call is here
req_arg()               #dafault arguments
req_arg("hello",3)      #keyword arguments
req_arg("&",2,3)



print("=================================================")
print ("\nUse of lambda : \n")

#function definition is here
def sum (arg1, arg2):
    #add both the parameters and return sum.
    total = arg1 + arg2
    print ("inside the function : ", total)
    return total

#function call is here
total = sum (10,20)
print ("outside the function : ", total)


print("=================================================")
print ("\nGlobal vs Local variables : \n")


total = 0;
#function definition is here
def sum (arg1, arg2):
    #add both the parameters and return sum.
    total = arg1 + arg2
    print ("inside the function : ", total)
    return total

#function call is here
total1 = sum (10,20)
print ("outside the function : ", total)

print ("outside the function : ", total1)








#!/usr/bin/python

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

 

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
