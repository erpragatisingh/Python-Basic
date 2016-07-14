class student :
    "Common base class for all students"
    studentCount = 0

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        student.studentCount += 1


    def displayCount(self):
        print ("total student %d" %student.studentCount)

    def displa
