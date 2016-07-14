##Library Functions
print ("\n===================================================")
print ("\n 1. Maths\n")

import math

print (math.cos(math.pi/4))   #cos(pi/4)= 1/sqrt2
print (math.sqrt(1/2))
print (math.sqrt(3))
print (math.log(1024, 2))

print ("\n===================================================")
print ("\n 2. Random\n")
 
import random


print (random.choice(['apple', 'pear', 'banana']))
print (random.sample(range(100),10))   #sampling without replacement
print (random.random())
print (random.randrange(6))              #random integer

print ("\n===================================================")
print ("\n 3. Statistics\n")

import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print (statistics.mean(data))
print (statistics.median(data))
print (statistics.variance(data))


print ("\n===================================================")
print ("\n 4. OS\n")

import os

print (os.system)
