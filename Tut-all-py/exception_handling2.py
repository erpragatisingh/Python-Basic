#Exception handling and Error

def this_fails():
    x =1/0


try:
    this_fails()
except  ZeroDivisionError as err:
    #print ("cant devide by 0")
    print ("Handling run_time error: ", err)
