##8. Errors and Exceptions
##Until now error messages haven’t been more than mentioned, but if you have tried out the examples you have probably seen some. There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

##8.1. Syntax Errors
##Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:

##while True print('Hello world')

##>>> while True print('Hello world')
##  File "<stdin>", line 1, in ?
##    while True print('Hello world')
##                   ^
##SyntaxError: invalid syntax

##The parser repeats the offending line and displays a little ‘arrow’ pointing at the earliest point in the line where the error was detected. The error is caused by (or at least detected at) the token preceding the arrow: in the example, the error is detected at the function print(), since a colon (':') is missing before it. File name and line number are printed so you know where to look in case the input came from a script.

##8.2. Exceptions

##Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages as shown here:

#10 * (1/0)
#4 + spam*3
#'2' + 2

##The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError. The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention). Standard exception names are built-in identifiers (not reserved keywords).

##The rest of the line provides detail based on the type of exception and what caused it.
##
##The preceding part of the error message shows the context where the exception happened, in the form of a stack traceback. In general it contains a stack traceback listing source lines; however, it will not display lines read from standard input.
##
##Built-in Exceptions lists the built-in exceptions and their meanings.
