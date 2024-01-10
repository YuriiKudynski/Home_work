class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def introduce(self):
        return f"My name is  {self.name}, age {self.age}"


class Student(Person):

    def __init__(self, name, age, person_id):
        super().__init__(name, age)
        self.person_id = person_id

    def study(self, subject):
        return f"Student {self.name} with ID {self.person_id} study {subject}"

    def introduce(self):
        print(f"My name is  {self.name}, age {self.age}. i Am student with ID {self.person_id}")


class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self, s):
        if isinstance(s, Student):
            print(f"{self.name} teach {self.subject} student {s.name}")
        else:
            print(f"{s.name} dont teach {self.subject}. {s.name} not a student")

    def introduce(self):
        print(f"My name is  {self.name}, age {self.age}. I am teacher and teach {self.subject}")


class Employee(Person):

    def __init__(self, name, age, salary, specialty):
        super().__init__(name, age)
        self.salary = salary
        self.specialty = specialty

    def work(self):
        return f"{self.name} work in {self.specialty} and have {self.salary} salary."

    def introduce(self):
        print(f"My name is  {self.name}, age {self.age}. I am Employee. Work in {self.specialty} and i have {self.salary}")


user1 = Person("Alice", 22)
print(user1.introduce)

user2 = Student("Gloria", 23, 1321)
user3 = Teacher("Ron", 35, "Math")
user4 = Employee("Peter", 31, "1500$", "Web-design")
print()

user2.introduce()
print(user2.study("Math"))
print()

user3.introduce()
user3.teach(user1)
user3.teach(user2)
print()

user4.introduce()
print(user4.work())
print()

print(Person.mro())
print(Student.mro())
print(Teacher.mro())
print(Employee.mro())