##Python Program to Print all Prime Numbers in an Interval

num = int(input("Enter a number: "))

for n in range (2, num+1):
    for i in range (2, n):
        if (n % i) == 0:
            print (n ,"is a prime not a number")
            break
    else:
        print (n, "is a pime number")
        
    
        
