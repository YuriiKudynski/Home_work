import math


class Circle:

    def __init__(self, r=1):
        self.r = r

    def __str__(self):
        return f'Circle radius is {self.r}'

    def square_circle(self):
        return math.pi * (self.r ** 2)

    def len_circle(self):
        return 2 * math.pi * self.r


circle1 = Circle(2)
print(circle1)
print(f'Area: {circle1.square_circle():.2f}')
print(f"Len circle: {circle1.len_circle():.2f}")

print()

circle2 = Circle(3)
print(circle2)
print(f"Area: {circle2.square_circle():.2f}")
print(f"Len circle: {circle2.len_circle():.2f}")