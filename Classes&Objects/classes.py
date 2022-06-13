#custom dataType like string  int and bool but has alot in it
#You can model a custom datatype and use it multiple times with different instances called objects
#Similar to struct in C programming language
class Student:
    def __init__(self, name,major,gpa,isOnLeave):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.isOnLeave = isOnLeave

class Teacher:
    def __init__(self, name,position,subject,isOnLeave):
        self.name = name
        self.major = position #postion is name of paramter can have differnt name disognation
        self.subject = subject
        self.isOnLeave = isOnLeave
    
    def teacherClass(self):
        print("Teaches " + self.subject)