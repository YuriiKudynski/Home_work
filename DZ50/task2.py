class Car:
    producer = "Volkswagen auto group(VAG)"
    total = 0

    def __init__(self, model, year, engine, color, price):
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price

        Car.total += self.price

    def __str__(self):
        return f"""\nCar Model: {self.model}
Producer: {self.producer}
Year: {str(self.year)}
Engine: {str(self.engine)}L
Color: {self.color}
Price: {str(self.price)}$"""

    def change_color(self, new_color):
        self.color = new_color
        print(f"Change color from {self.color} to {new_color}")

    def change_price(self, new_price):
        Car.total -= self.price
        self.price = new_price
        Car.total += new_price
        print(f"Change price from {self.price} to {new_price}")

    @classmethod
    def get_total(cls):
        return cls.total


car1 = Car("Volkswagen Golf", 2004, 1.8, "Gray", 5000)
car2 = Car("Audi A4", 2008, 2.0, "Black", 8000)

car2.change_color("Green")
car1.change_price(3000)

print(car1)
print(car2)

print(f"\nTotal price of all cars = {Car.total}$")

print(f"\nTotal Price of all cars(object): {car1.get_total()}$")
print(f"Total Price of all cars(class): {Car.get_total()}$")
