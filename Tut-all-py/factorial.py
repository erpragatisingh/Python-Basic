print("""The factorial of a number is the product of all the integers from 1 to that number.
For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.
Factorial is not defined for negative numbers and the factorial of zero is one, 0! = 1""")

print("i have to calculate factorial of 10:")

n=10
i=1
f=1

for i in range(1,11):
    f = f*i
    print ("i =", i,",f =", f)
    i += 1

print("the factorial of 10 is :", f)

print ("\n")
print ("Output should be:")
print ("\n")
print ("""The factorial of a number is the product of all the integers from 1 to that number.
For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.
Factorial is not defined for negative numbers and the factorial of zero is one, 0! = 1
i have to calculate factorial of 10:
i = 1 ,f = 1
i = 2 ,f = 2
i = 3 ,f = 6
i = 4 ,f = 24
i = 5 ,f = 120
i = 6 ,f = 720
i = 7 ,f = 5040
i = 8 ,f = 40320
i = 9 ,f = 362880
i = 10 ,f = 3628800
the factorial of 10 is : 3628800""")

