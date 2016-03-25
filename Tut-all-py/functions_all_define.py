print("""A function is a block of organized, reusable code that is used
to perform a single, related action. Functions provide better modularity for
your application and a high degree of code reusing.

As you already know, Python gives you many built-in functions like print(),
etc. but you can also create your own functions. These functions are called
user-defined functions.""")


print("""\n Defining a Function
You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).

Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.

The first statement of a function can be an optional statement - the documentation string of the function or docstring.

The code block within every function starts with a colon (:) and is indented.

The statement return [expression] exits a function, optionally passing back an expression to the caller.
A return statement with no arguments is the same as return None.\n""")

#

#def functionname( parameters ):
#   "function_docstring"
#   function_suite
#   return [expression]
#
print("defin a Function")
def printme( str ):
  # "This prints a passed string into this function"
   print (str)
   return
print("Calling a Function")


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


print("\n Pass by reference vs value\n")

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)





print("""Function Arguments
You can call a function by using the following types of formal arguments:

Required arguments

Keyword arguments

Default arguments

Variable-length arguments""")


print("Required arguments \n\n To call the function printme(), you definitely need to pass one argument, otherwise it gives a syntax error as follows")

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
#printme() ## due to error commentrd for now


print("""Keyword arguments
Keyword arguments are related to the function calls. When you use
keyword arguments in a function call, the caller identifies the arguments by
the parameter name.

This allows you to skip arguments or place them out of order because
the Python interpreter is able to use the keywords provided to match
the values with parameters. You can also make keyword calls to the printme()
function in the following ways −""")


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call printme function
printme( str = "\n My string using Keyword arguments")

# Function definition is here
def printinfo( namea, age ):
   "This prints a passed info into this function"
   print ("Name: ", namea)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, namea="miki" )


print("\n Default arguments\n")

print(""""A default argument is an argument that assumes a
default value if a value is not provided in the function call for that
argument. The following example gives an idea on default arguments,
it prints default age if it is not passed −""")


# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )


print("\n Variable-length arguments \n")

print("""You may need to process a function for more arguments than you
specified while defining the function. These arguments are called
variable-length arguments and are not named in the function definition,
unlike required and default arguments.

Syntax for a function with non-keyword variable arguments is this −

def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]
An asterisk (*) is placed before the variable name that holds the values of
all nonkeyword variable arguments. This tuple remains empty if no additional
arguments are specified during the function call. Following is a simple example """)
      

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )     
      
print("""\n The Anonymous Functions
These functions are called anonymous because they are not declared in the
standard manner by using the def keyword. You can use the lambda keyword to
create small anonymous functions.

Lambda forms can take any number of arguments but return just one value in
the form of an expression. They cannot contain commands or multiple expressions.

An anonymous function cannot be a direct call to print because lambda
requires an expression

Lambda functions have their own local namespace and cannot access
variables other than those in their parameter list and those in the global
namespace.

Although it appears that lambda's are a one-line version of a function,
they are not equivalent to inline statements in C or C++, whose purpose is by
passing function stack allocation during invocation for performance reasons.\n """)


# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

 

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

print("\nThe return Statement\n")

# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total;

# Now you can call sum function
total = sum( 10, 20 );
print ("Outside the function : ", total )


print("Global vs. Local variables")

total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total )






