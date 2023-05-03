class Human():
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Your name: " +self.name)
        print("Your age: " + str(self.age))

class Student(Human):
    def __init__ (self, name, age  ,sutdentnum):
        super().__init__(self, name, age)
        self.studentnum = sutdentnum
    
    def display_student(self):
        print("Your sudent number: " + str(self.studentnum))

me = Human("Max Muster", 30)
me.display()

alsome = Student("Leon Ranke", 24, 1234)
alsome.display()
alsome.display_student()
