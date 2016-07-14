class Parent :                  # define parent class
    def myMethod(self):
        print ("calling parent mathod")

class Child (Parent):                   # define child class
    def myMethod(self):
        print ("calling child method")

c = Child()                     # instance of child
c.myMethod()                    # child calls overridden method



###################################################################

class Parent1 :                  # define parent class
    def myMethod(self):
        print ("calling parent mathod")

class Child1 :                   # define child class
    def myMethod(self):
        print ("calling child method")
        

c1 = Child1()                     # instance of child
c1.myMethod()                     # no overridding as no inheritance


###################################################################
#polymorphism means that the meaning of an operation depends on the object being operated on

class Employee :                # general superclass
    def computeSalary(self):    # Common or default behaviors
        print ("print the salary of this employee")
    def giveRaise(self):
        print ("print the salary raise of this employee")
    def promote(self):
        print ("print the designation of this employee")
    def retire(self):
        print ("print the retirement date of this employee")



class Engineer (Employee) :     # specialized subclass
    def computeSalary(self):    # Something custom here
        print ("print the salary of this engineer")


bob = Employee()                # default behavior
sue = Employee()                # default behavior
tom = Engineer()                # custom salary calculator


company = [bob, sue, tom]       # a composite object
for emp in company:
    print (emp.computeSalary()) # Run this object's version: default or custom
