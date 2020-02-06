class Student:
    def __init__(self):
        self.name=input("Enter student name: ") #replace self with Student
        self.roll=eval(input("Enter roll number: "))
        self.stream=input("Enter stream: ")
    def Show(self):
        print("Student- ", self.name) #replace self with Student
        print("Roll number- ", self.roll)
        print("Stream- ", self.stream)
ob=Student()
ob.Show()