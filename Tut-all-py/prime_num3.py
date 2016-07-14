# Python program to check if the input number is prime or not

# take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")


##In this program, user is asked to enter a number and this program check whether that number is prime or not. Numbers less than or equal to 1 are not prime numbers. Hence, we only proceed if the num is greater than 1. We check if num is exactly divisible by any number from 2 to num - 1. If we find a factor in that range, the number is not prime. Else the number is prime.

##We can decrease the range of numbers where we look for factors. In the above program, our search range is from 2 to num - 1. We could have used the range, [2, num / 2] or [2, num ** 0.5]. The later range is based on the fact that a composite number must have a factor less than square root of that number. Otherwise the number is prime.
