import time;  # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)

print("TimeTuple")


print("""Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −

Index	Field	Values
0	4-digit year	2008
1	Month	1 to 12
2	Day	1 to 31
3	Hour	0 to 23
4	Minute	0 to 59
5	Second	0 to 61 (60 or 61 are leap-seconds)
6	Day of Week	0 to 6 (0 is Monday)
7	Day of year	1 to 366 (Julian day)
8	Daylight savings	-1, 0, 1, -1 means library determines DST""")


print("The above tuple is equivalent to struct_time structure. This structure has following attributes")

print("""Index	Attributes	Values
0	tm_year	2008
1	tm_mon	1 to 12
2	tm_mday	1 to 31
3	tm_hour	0 to 23
4	tm_min	0 to 59
5	tm_sec	0 to 61 (60 or 61 are leap-seconds)
6	tm_wday	0 to 6 (0 is Monday)
7	tm_yday	1 to 366 (Julian day)
8	tm_isdst	-1, 0, 1, -1 means library determines DST""")


print("Getting current time")

import time;

localtime = time.localtime(time.time())
print ("\nLocal current time :\n", localtime)

print("Getting formatted time")

import time;

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

print("Getting calendar for a month")

import calendar

cal = calendar.month(2016, 1)
print ("Here is the calendar:")
print (cal)


help (calendar)

help(time)











