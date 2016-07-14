#Exception handling and Error

while 1:
    try:
        x = int(input("Please enter any number: "))
        print ("Provided number is : ",x)
        break
    except  ValueError  :
        print ("Oops! that was not a valid number. Try again...")
