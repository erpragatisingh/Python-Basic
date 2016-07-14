print ("Python Program to Check Prime Number")

print ("\n")
print ("""A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number.
2, 3, 5, 7 etc. are prime numbers as they do not have any other factors.
But 6 is not prime (it is composite) since, 2 x 3 = 6.""")


print ("\n")        
print ("for input number")

num = int(input("enter a number to check prime or not: "))
print ("entered number is :", num)

if num > 1:
    for i in range (2, num):
        if (num % i) == 0:
            print (num ,"is not a prime number")
            break
    else :
        print (num ,"is a prime number")

else:
    print (num ,"is not a prime number")

##for i in range (2,10):
  ##  print (i)
