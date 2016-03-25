import time;

localtime = time.localtime(time.time())
print ("Local current time :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


import calendar

cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)
