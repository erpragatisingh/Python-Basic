##Python Program to Find Factors of Number

num = int(input("Enter a number to find factors : "))

for i in range (2,num):
    if (num % i) == 0:
        print (i, "is a factor")
        a[i] = i

print (a)

