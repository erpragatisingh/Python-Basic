# Python break statement

print("\n Python nested loops \n")

for letter in 'Python':     # First Example
   print(letter)
   if letter == 'h':
      
      break
   print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break

print "Good bye!"
