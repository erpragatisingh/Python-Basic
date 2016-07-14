class FirstClass :                  # define a class object
    def setdata(self, value):       # define class's methods
        self.data = value           # self is the instance
    def display(self):
        print (self.data)           #self.data:per instance


x = FirstClass()                    # Make two instances
y = FirstClass()                    # Each is a new namespace

x.setdata("king arthur")            # call methods:self is x
y.setdata(3.14159)                  # runs : FirstClass.setdata(y, 3.14159)



x.display()                         # self.data differs in each instance
y.display()                         # Runs: FirstClass.display(y)


x.data = "New value"                # Can get/set attributes
x.display()                         # self.data differs in each instance


x.anothername = "spam"              # Can set new attributes here too!
x.display() 


class SecondClass(FirstClass):      # inherits setdata
    def display(self):              # changes display
        print ('current value = "%s"' %self.data)


z = SecondClass()
z.setdata(42)                       # finds setdata in FirstClass
z.display()                         # finds overridden method in SecondClass  


x.display()                         # x is still a FirstClass instance (old message)


###################################################################################

class Parent :                      # define a parent class
    parentAttr = 100
    def __init__(self):
        print ("calling parent constructor")
    def parentMethod(self):
        print ("calling parent method")
    def setAttr(self,attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print ("Parent attribute : ", Parent.parentAttr)

class Child(Parent) :               # define child class
    def __init__(self):
        print ("calling child constructor")
    def childMethod(self):
        print ("calling child method")

c = Child()                         # instance of child
c.childMethod()                     # child calls its method
c.parentMethod()
c.getAttr()                         # calls parent method

c.setAttr(200)                      # again call parent's method
c.getAttr()                         # again call parent's method
        
    
