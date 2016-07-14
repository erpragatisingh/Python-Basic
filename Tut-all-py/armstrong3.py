#Python Program to Find Armstrong Number in an Interval
#An Armstrong number, also known as narcissistic number, is a number that is equal to the sum of the cubes of its own digits. For example, 371 is an Armstrong number since 371 = 3*3*3 + 7*7*7 + 1*1*1.

# Program to ask the user for a range and display all Armstrong numbers in that interval

# take input from the user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper + 1):
   # initialize sum
   sum = 0

   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

   if num == sum:
       print(num)
