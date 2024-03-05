import json
from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, manufacturer: str, year: int, model: str, cost_price: float, quantity: int):
        self.manufacturer = manufacturer
        self.year = year
        self.model = model
        self.cost_price = cost_price
        self.quantity = quantity

    @abstractmethod
    def display_details(self):
        pass

    def update_json(self):
        with open("cars.json", 'r') as file:
            data = json.load(file)
            for car_data in data:
                if car_data['manufacturer'] == self.manufacturer and car_data['model'] == self.model:
                    car_data['sold'] = True
                    break
        with open("cars.json", 'w') as file:
            json.dump(data, file, indent=4)

    def is_sold(self) -> bool:
        return self.quantity == 0

    def sell(self):
        if self.quantity > 0:
            self.quantity -= 1
            print("Car sold successfully.")
            self.update_json()


class CarInventory(ABC):
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)
        self.save_to_json("cars.json")

    def remove_car(self, car: Car):
        self.cars.remove(car)
        self.save_to_json("cars.json")

    @abstractmethod
    def get_car(self, index: int):
        pass

    def save_to_json(self, filename: str):
        data = [car.__dict__ for car in self.cars]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for car_data in data:
                    quantity = car_data.get('quantity', 1)
                    car = CarImplementation(car_data['manufacturer'], car_data['year'], car_data['model'],
                                            car_data['cost_price'], quantity)
                    self.cars.append(car)
        except FileNotFoundError:
            print("No existing data found.")

    def display_car_info(self):
        if not self.cars:
            print("No cars in inventory.")
        else:
            print("Car Information:")
            for car in self.cars:
                print(
                    f"Manufacturer: {car.manufacturer}, Model: {car.model}, Year: {car.year}, Cost Price: {car.cost_price}, Quantity Left: {car.quantity}")


class Employee(ABC):
    def __init__(self, last_name: str, first_name: str, position: str):
        self.last_name = last_name
        self.first_name = first_name
        self.position = position

    @abstractmethod
    def display_details(self):
        pass


class EmployeeRegistry(ABC):
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        self.save_to_json("employees.json")

    def remove_employee(self, employee: Employee):
        self.employees.remove(employee)
        self.save_to_json("employees.json")

    @abstractmethod
    def get_employee(self, index: int) -> Employee:
        pass

    def save_to_json(self, filename: str):
        data = [emp.__dict__ for emp in self.employees]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for emp_data in data:
                    employee = EmployeeImplementation(emp_data['last_name'], emp_data['first_name'], emp_data['position'])
                    self.employees.append(employee)
        except FileNotFoundError:
            print("No existing data found.")


class Sale(ABC):
    def __init__(self, employee: Employee, car: Car, actual_price: float):
        self.employee = employee
        self.car = car
        self.actual_price = actual_price

    def to_dict(self) -> dict:
        return {
            "employee": self.employee.__dict__,
            "car": self.car.__dict__,
            "actual_price": self.actual_price
        }

    def profit(self) -> float:
        return self.actual_price - self.car.cost_price


class SalesManager(ABC):
    def __init__(self):
        self.sales_records = []

    def manage_sale_record(self, sale_record: Sale, operation: str):
        if operation == "add":
            for record in self.sales_records:
                if self.is_same_sale(record, sale_record):
                    record.actual_price = sale_record.actual_price
                    self.save_to_json("sales.json")
                    print("Sale record updated successfully.")
                    return
            self.sales_records.append(sale_record)
        elif operation == "remove":
            self.sales_records.remove(sale_record)
        self.save_to_json("sales.json")

    def is_same_sale(self, record1: Sale, record2: Sale) -> bool:
        return record1.employee.last_name == record2.employee.last_name \
               and record1.employee.first_name == record2.employee.first_name \
               and record1.car.manufacturer == record2.car.manufacturer \
               and record1.car.model == record2.car.model

    def display_employee_sales_info(self):
        print("Employee Sales Information:")
        for record in self.sales_records:
            print(
                f"Employee: {record.employee.last_name} {record.employee.first_name}, Car: {record.car.manufacturer} {record.car.model}, Actual Price: {record.actual_price}")

    def display_car_info(self, car_inventory: CarInventory = None):
        if car_inventory is None:
            print("No car inventory provided.")
            return
        car_inventory.display_car_info()

    def calculate_profit(self) -> float:
        return sum(record.profit() for record in self.sales_records)

    def display_sales_info(self):
        print("Sales Information:")
        for record in self.sales_records:
            print(
                f"Car: {record.car.manufacturer} {record.car.model}, Sold by: {record.employee.last_name} {record.employee.first_name}, Actual Price: {record.actual_price}")

    def save_to_json(self, filename: str):
        data = [sale_record.to_dict() for sale_record in self.sales_records]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for sale_data in data:
                    employee_data = sale_data['employee']
                    car_data = sale_data['car']
                    employee = EmployeeImplementation(employee_data['last_name'], employee_data['first_name'],
                                                       employee_data['position'])
                    car = CarImplementation(car_data['manufacturer'], car_data['year'], car_data['model'],
                                            car_data['cost_price'], car_data['quantity'])
                    actual_price = sale_data['actual_price']
                    sale_record = Sale(employee, car, actual_price)
                    self.sales_records.append(sale_record)
        except FileNotFoundError:
            print("No existing sales data found.")


class CarImplementation(Car):
    def display_details(self):
        print(
            f"Manufacturer: {self.manufacturer}, Year: {self.year}, Model: {self.model}, Cost Price: {self.cost_price}")

    def sell(self):
        if self.quantity > 0:
            self.quantity -= 1
            print("Car sold successfully.")
            self.update_json()


class CarInventoryImplementation(CarInventory):
    def get_car(self, manufacturer, model) -> Car:
        for car in self.cars:
            if car.manufacturer == manufacturer and car.model == model:
                return car
        return None

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for car_data in data:
                    quantity = car_data.get('quantity', 1)
                    car = CarImplementation(car_data['manufacturer'], car_data['year'], car_data['model'],
                                            car_data['cost_price'], quantity)
                    self.cars.append(car)
        except FileNotFoundError:
            print("No existing data found.")


class EmployeeImplementation(Employee):
    def display_details(self):
        print(f"Employee: {self.last_name} {self.first_name}, Position: {self.position}")


class EmployeeRegistryImplementation(EmployeeRegistry):
    def get_employee(self, index: int):
        return self.employees[index]

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for emp_data in data:
                    employee = EmployeeImplementation(emp_data['last_name'], emp_data['first_name'], emp_data['position'])
                    self.employees.append(employee)
        except FileNotFoundError:
            print("No existing data found.")


class SalesManagerImplementation(SalesManager):
    def __init__(self):
        super().__init__()
        self.load_from_json("sales.json")

    def add_sale(self, sale_record: Sale):
        self.manage_sale_record(sale_record, "add")

    def remove_sale(self, sale_record: Sale):
        self.manage_sale_record(sale_record, "remove")

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for sale_data in data:
                    employee_data = sale_data['employee']
                    car_data = sale_data['car']
                    employee = EmployeeImplementation(employee_data['last_name'], employee_data['first_name'],
                                                       employee_data['position'])
                    car = CarImplementation(car_data['manufacturer'], car_data['year'], car_data['model'],
                                            car_data['cost_price'], car_data['quantity'])
                    actual_price = sale_data['actual_price']
                    sale_record = Sale(employee, car, actual_price)
                    self.sales_records.append(sale_record)
        except FileNotFoundError:
            print("No existing sales data found.")


def main():
    car_inventory = CarInventoryImplementation()
    employee_registry = EmployeeRegistryImplementation()
    sales_manager = SalesManagerImplementation()

    try:
        employee_registry.load_from_json("employees.json")
        car_inventory.load_from_json("cars.json")
        sales_manager.load_from_json("sales.json")
    except FileNotFoundError:
        print("No existing data found.")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            for employee in employee_registry.employees:
                employee.display_details()
        elif choice == '2':
            car_inventory.display_car_info()
        elif choice == '3':
            sales_manager.display_employee_sales_info()
        elif choice == '4':
            add_employee(employee_registry)
        elif choice == '5':
            add_car(car_inventory)
        elif choice == '6':
            add_sale(sales_manager, employee_registry, car_inventory)
        elif choice == '7':
            display_profit(sales_manager)
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def display_menu():
    print("\nMenu:")
    print("1. Show employees")
    print("2. Show remaining cars")
    print("3. Show sales by employees")
    print("4. Add an employee")
    print("5. Add a car")
    print("6. Add a sale")
    print("7. Display profit")
    print("8. Exit")


def add_employee(employee_registry: EmployeeRegistry):
    while True:
        try:
            last_name = input("Enter employee's last name: ")
            first_name = input("Enter employee's first name: ")
            position = input("Enter employee's position: ")
            new_employee = EmployeeImplementation(last_name, first_name, position)
            employee_registry.add_employee(new_employee)
            employee_registry.save_to_json("employees.json")
            print("Employee added successfully.")
            break
        except Exception as e:
            print(f"Error: {e}")
            choice = input("Do you want to try again? (yes/no): ")
            if choice.lower() != 'yes':
                break


def add_car(car_inventory: CarInventory):
    while True:
        try:
            manufacturer = input("Enter car manufacturer: ")
            year = int(input("Enter car year: "))
            model = input("Enter car model: ")
            cost_price = float(input("Enter car cost price: "))
            quantity = int(input("Enter quantity: "))
            new_car = CarImplementation(manufacturer, year, model, cost_price, quantity)
            car_inventory.add_car(new_car)
            print("Car added successfully.")
            break
        except Exception as e:
            print(f"Error: {e}")
            choice = input("Do you want to try again? (yes/no): ")
            if choice.lower() != 'yes':
                break


def add_sale(sales_manager: SalesManager, employee_registry: EmployeeRegistry, car_inventory: CarInventory):
    while True:
        try:
            print("Add a sale:")
            employee_name = input("Enter employee's last name or first name: ")
            car_manufacturer = input("Enter car manufacturer: ")
            car_model = input("Enter car model: ")  # Ініціалізуємо змінну car_model перед викликом get_car
            actual_price = float(input("Enter actual price of the car sold: "))

            employee = next((emp for emp in employee_registry.employees if
                             emp.last_name == employee_name or emp.first_name == employee_name), None)
            car = car_inventory.get_car(car_manufacturer, car_model)

            if employee is None:
                raise ValueError("Employee not found.")
            if car is None:
                raise ValueError("Car not found, or out of stock.")

            new_sale = Sale(employee, car, actual_price)
            sales_manager.add_sale(new_sale)
            car.sell()
            print("Sale added successfully.")
            break
        except Exception as e:
            print(f"Error: {e}")
            choice = input("Do you want to try again? (yes/no): ")
            if choice.lower() != 'yes':
                break


def display_profit(sales_manager: SalesManager):
    profit = sales_manager.calculate_profit()
    print(f"Total profit: ${profit}")


if __name__ == "__main__":
    main()
