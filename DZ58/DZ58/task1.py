class Size:
    def __get__(self, instance, owner):
        return len(instance.name)


class Person:
    size_name = Size()

    def __init__(self, name):
        self.name = name


person1 = Person("John")
print(person1.size_name)

