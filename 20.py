class Student:
    university = "SDU" 
    name = "Beks"
    age = 19

    def info(self):
        return f"Name: {self.name}, age: {self.age}, university: {self.university}"

chel = Student()
print(chel.info())

Student.university = "KBTU"
print(chel.info())