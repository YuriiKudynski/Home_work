def student_init(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender


def student_greet(self):
    print(f"Hi, my name is {self.name}")


def student_description(self):
    print(f"Person <{self.name}, {self.age}, {self.gender}>")


Student = type("Student", (object,), {
    "team": "Python31",
    "__slots__": ["name", "age", "gender"],
    "__init__": student_init,
    "greet": student_greet,
    "description": student_description,
    })

student1 = Student("Alice", 20, "Female")
student1.greet()
student1.description()
