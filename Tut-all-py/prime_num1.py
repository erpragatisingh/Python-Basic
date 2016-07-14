print ("Python Program to Check Prime Number")

print ("\n")
print ("""A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
2, 3, 5, 7 etc. are prime numbers as they do not have any other factors.
But 6 is not prime (it is composite) since, 2 x 3 = 6.""")

print ("\n")
print ("1st check for number : 10")

for i in range (2,10):
    x = 10%i
    if x == 0:
        print ("10 is not a prime number as it is divisible by", i)
        break
    else:
        print ("10 is a prime number")


print ("\nWithout using break")
for i in range (2,10):
    x = 10%i
    if x == 0:
        print ("10 is not a prime number as it is divisible by", i)

        
print ("\n")        
print ("2nd check for number : 11")

for i in range (2,11):
    x = 11%i
    if x == 0:
        print ("11 is not a prime number as it is divisible by", i)
        break
if x != 0:
    print ("11 is a prime number")
    



print ("\nWithout using break")
for i in range (2,11):
    x = 11%i
    if x == 0:
        print ("11 is not a prime number as it is divisible by", i)
        break
    else:
        print ("11 is a prime number")





