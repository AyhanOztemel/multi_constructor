class Student:
    def __init__(self, name=None, age=None, classroom=None,address=None):
        self.name = name
        self.age = age
        self.classroom = classroom
        self.address=address
        self.__multi_init()

    def __multi_init(self):
        ", ".join(f"{k}: {v}" for k, v in self.__dict__.items() if v)
        


    
    
student1 = Student("Ali", 15, 9,"kartal")
print(student1.name,student1.age,student1.classroom,student1.address)

student2 = Student("Ayşe", 14)
print(student2.name,student2.age,student2.classroom)

student3 = Student("Mehmet")
print(student3.name,student3.age,student3.classroom)

student4 = Student()
print(student4.name,student4.age,student4.classroom)




