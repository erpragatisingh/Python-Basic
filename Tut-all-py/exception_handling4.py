try:
    x = 10 * (1/0)
except ZeroDivisionError as error:
    print ("exception is handled here :", error)
    



try:
    4 + hhh*3
except NameError as err:
    print ("exception is handled here : ", err)
