import math
from abc import ABCMeta, abstractmethod


class IShape(metaclass=ABCMeta):

    @abstractmethod
    def get_area(self) -> float:
        pass


class Shape(IShape):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def info(self):
        pass


class Square(Shape):

    def __init__(self, side: float, name: str):
        super().__init__(name)
        self.side = side

    def info(self):
        print(f"{self.name} {self.side}")

    def get_area(self) -> float:
        return self.side * self.side


class Circle(Shape):

    def __init__(self, radius: float, name: str):
        super().__init__(name)
        self.radius = radius

    def info(self):
        print(f"{self.name} {self.radius}")

    def get_area(self) -> float:
        return math.pi * self.radius * self.radius


circle = Circle(3.5, "Margarita")
square = Square(3.8, "New York")


class Pizza:

    def __init__(self, price: float, shape: IShape):
        self.__price = price
        self.__shape = shape

    def get_price(self) -> float:
        return self.__price * self.__shape.get_area()

    def get_shape_class(self) -> None:
        print(self.__shape.__class__.__name__)

    def cut_pizza(self):
        print(f"I bought pizza with name {self.__shape.name}")


pizza = Pizza(34, circle)
print(pizza.get_price())
pizza.get_shape_class()
pizza.cut_pizza()
