class Person:
    """Опис класу.
       Ці рядки автоматично можна продивитись функцією help """
    def __init__(self, name, money=0):
        self.name = name
        self.money = money
        self.friends = []
        print(f"A new Person is born! -> {self.name}")

    def __str__(self):
        return self.name + str(self.money)

    def give_money(self, delta):
        self.money += delta
        print(f"Рахунок {self.name} поповнено на суму {delta}, всього = {self.money}")

    def add_money(self, amount):
        self.money += amount
        print(f"Рахунок {self.name} поповнено на суму {amount}, всього = {self.money}")

    def know(self, person):
        self.friends.append(person.name)

    def is_know(self, person):
        return person.name in self.friends


A = Person("Vasyl")
B = Person("Kateryna")
C = Person("Petro", 10)
D = Person("Ira", 30)
print()

B.money = 100.2852
A.give_money(50.127)
B.give_money(40)

people = [A, B, C, D]

for p in people:
    if p.money < 50:
        p.add_money(100)

print(f"\nA: Name = {A.name}, money = {A.money:.2f}")
print(f"B: Name = {B.name}, money = {B.money:.2f}")
print(f"C: Name = {C.name}, money = {C.money:.2f}")
print(f"D: Name = {D.name}, money = {D.money:.2f}\n")

A.know(B)
B.know(C)
C.know(D)

print(f"A know B? -> {A.is_know(B)}")
print(f"B know D? -> {B.is_know(D)}")


