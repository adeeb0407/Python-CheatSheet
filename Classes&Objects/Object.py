from classes import Student
import classes # importing the class Student from classes.py 

student1 = Student("Adeeb", "Computer Science", 4.2, False); #instance of an Class is an object and here class named Student is the class and the object is anmed student1
student2 = Student("Adnan", "Business Management", 3.6, True)

print(student1.name + '\n' + student1.major)
print(student2.major)
teacher1 = classes.Teacher("Imran", "Principal", "English", False)

print(teacher1.major) # paramerter is position name and the name on the class is major

teacher1.teacherClass(); #creating object funtions calling fuctnion of class