class FirstClass :                  # define a class object
    def __init__(self, value):       # define class's methods
        self.data = value
        print (self.data)               # self is the instance
#    def display(self):
                                           #self.data:per instance


x = FirstClass("king arthur")                    # Make two instances
y = FirstClass(3.14159)                    # Each is a new namespace

#x.setdata("king arthur")            # call methods:self is x
#y.setdata(3.14159)                  # runs : FirstClass.setdata(y, 3.14159)



#x.display()                         # self.data differs in each instance
#y.display()                         # Runs: FirstClass.display(y)


#############################################################

class FirstClass :                   # define a class object
    def __init__(self, value):       # define class's methods
        self.data = value            # self is the instance
    def display(self):
        print (self.data)            #self.data:per instance


x = FirstClass("king arthur")                    # Make two instances
y = FirstClass(3.14159)                    # Each is a new namespace

#x.setdata("king arthur")            # call methods:self is x
#y.setdata(3.14159)                  # runs : FirstClass.setdata(y, 3.14159)



x.display()                         # self.data differs in each instance
y.display()                         # Runs: FirstClass.display(y)
