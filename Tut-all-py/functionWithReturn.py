# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total;

# Now you can call sum function
total = sum( 10, 20 );
print ("Outside the function : ", total)


def print_welcome(name):

    return 'Welcome '+name+" !"


print(print_welcome('Pragati'))


import fibo, sys


dir(sys) # to view all defined function under sys module
dir(fibo)
