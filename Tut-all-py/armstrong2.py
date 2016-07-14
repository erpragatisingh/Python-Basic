#Python Program to Find Armstrong Number in an Interval
#An Armstrong number, also known as narcissistic number, is a number that is equal to the sum of the cubes of its own digits. For example, 371 is an Armstrong number since 371 = 3*3*3 + 7*7*7 + 1*1*1.

#num = int(input("Enter a number to check armstrong : "))

for num in range (1,1000):
    num1 = num
    sum = 0

    while num > 0:

        r = num%10
        sum = sum + r*r*r
        num = int(num/10)


    if num1 == sum:
        print (num1, "is an armstrong number")
    else:
        print (num1, "is not an armstrong number")
