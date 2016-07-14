## Python Program to Print all Prime Numbers in an Interval
# A positive integer greater than 1 which has no other factors except 1 and the number
# itself is called a prime number. 2, 3, 5, 7 etc. are prime numbers as they do not have
 # any other factors. But 6 is not prime (it is composite) since, 2 x 3 = 6. We ask the user
## for a range and display all the primes in that interval.


# Python program to ask the user for a range and display all the prime numbers in that
# interval

# take input from the user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

list1 = []
for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
           list1.append(num)

print (list1)
