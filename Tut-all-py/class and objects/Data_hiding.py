print("""

An object's attributes may or may not be visible outside
the class definition. You need to name attributes with a double underscore
prefix, and those attributes then are not be directly visible to outsiders.




When the above code is executed, it produces the following result −

1
2
Traceback (most recent call last):
  File "test.py", line 12, in <module>
    print counter.__secretCount
AttributeError: JustCounter instance has no attribute '__secretCount'
Python protects those members by internally changing the name to include the
class name. You can access such attributes as object._className__attrName.
If you would replace your last line as following, then it works for you −


""")


class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
# print (counter.__secretCount) # temp comment then use below example


print (counter._JustCounter__secretCount)
