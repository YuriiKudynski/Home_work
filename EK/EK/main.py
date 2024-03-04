import json
from abc import ABC, abstractmethod


class Car(ABC):
    """
        Абстрактний клас, який відповідає за створення автомобіля.
    """
    def __init__(self, manufacturer: str, year: int, model: str, cost_price: float, selling_price: float, quantity: int, quantity_left: int):
        """
            Ініціалізація класу
        :param manufacturer: Виробник
        :param year: Рік випуску
        :param model: Модель
        :param cost_price: Початкова вартість
        :param selling_price: Продажна вартість
        :param quantity: Кількість автомобілів для закупки
        :param quantity_left: Фактична кількість автомобілів що залишилась у наявності
        """
        self.manufacturer = manufacturer
        self.year = year
        self.model = model
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.quantity = quantity
        self.quantity_left = quantity_left
        self.sold = False

    @abstractmethod
    def display_details(self):
        """
        Абстрактний метод для відображення деталей автомобіля.
        """
        pass

    def sell(self):
        """
        Продаж автомобіля
        Помітка про продаж, оновлення кількості на залишку, оновлення запису у файлі JSON
        """
        if not self.sold and self.quantity_left > 0:
            self.sold = True
            self.quantity -= 1
            self.quantity_left -= 1
            print("Car sold successfully.")
            self.update_json()
        elif self.quantity_left == 0:
            print("This car is out of stock.")
        else:
            print("This car has already been sold.")

    def update_json(self):
        """
        Оновлення данних у JSON файлі після продажу автомобіля.
        """
        with open("cars.json", 'r') as file:
            data = json.load(file)
            for car_data in data:
                if car_data['manufacturer'] == self.manufacturer and car_data['model'] == self.model:
                    car_data['sold'] = True
                    break
        with open("cars.json", 'w') as file:
            json.dump(data, file, indent=4)

    def is_sold(self) -> bool:
        """
        Перевірка чи продано автомобіль
        :return:
        True - якщо продано, False - якщо ні
        """
        return self.sold


class CarInventory(ABC):
    """
    Абстрактний клас , який представляє інвертар автомобілів.
    """
    def __init__(self):
        """
        Ініціалізація обєкта класа CarInvertory.
        """
        self.cars = []

    def add_car(self, car: Car):
        """
        Додавання автомобіля до інвертаря

        Args:
            car (Car) : Екземпляр класу Car , який потрібно додати
        """
        self.cars.append(car)
        self.save_to_json("cars.json")

    def remove_car(self, car: Car):
        """
                Видалення автомобіля до інвертаря

                Args:
                    car (Car) : Екземпляр класу Car , який потрібно видалити
                """
        self.cars.remove(car)
        self.save_to_json("cars.json")

    @abstractmethod
    def get_car(self, index: int):
        """
                Абстрактний метод для отримання автомобіля з інвентаря за індексом.

                Args:
                    index (int): Індекс автомобіля у списку інвентаря.

                Returns:
                    Car: Екземпляр класу Car.
                """
        pass

    def save_to_json(self, filename: str):
        """
            Зберігає дані про автомобілі у JSON файл.

            Args:
                filename (str): Ім'я файлу для збереження даних.
        """
        data = [car.__dict__ for car in self.cars]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename: str):
        """
            Завантажує дані про автомобілі з JSON файлу.

            Args:
                filename (str): Ім'я файлу для завантаження даних.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            for car_data in data:
                quantity = car_data.get('quantity', 1)
                quantity_left = car_data.get('quantity_left', 1)
                car = CarImplementation(car_data['manufacturer'], car_data['year'], car_data['model'],
                                        car_data['cost_price'], car_data['selling_price'], quantity, quantity_left)
                self.cars.append(car)


class Employee(ABC):
    """
        Абстрактний клас, який представляє працівника.
    """

    def __init__(self, last_name: str, first_name: str, position: str):
        """
        Ініціалізація класу Employee
        :param last_name: Прізвище співробітника
        :param first_name: Імя співробітника
        :param position: Посада співробітника
        """
        self.last_name = last_name
        self.first_name = first_name
        self.position = position

    @abstractmethod
    def display_details(self):
        """
        Абстрактна функція для відображення деталей про працівника
        :return:
        """
        pass


class EmployeeRegistry(ABC):
    """
    Абстрактний клас , який веде реєстр співробітників
    """
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        """
        Додавання співробітнка до реєстру.
        :param employee: Екземпляр класу Employee, який потрібно додати.
        """
        self.employees.append(employee)
        self.save_to_json("employees.json")

    def remove_employee(self, employee: Employee):
        """
                Видалення співробітнка з реєстру.
                :param employee: Екземпляр класу Employee, якого потріно видалити з реєстру.
        """
        self.employees.remove(employee)
        self.save_to_json("employees.json")

    @abstractmethod
    def get_employee(self, index: int) -> Employee:
        """
            Абстрактний метод для отримання працівника з реєстру за індексом.

            Args:
                index (int): Індекс працівника у списку реєстру.

            Returns:
                    Employee: Екземпляр класу Employee.
        """
        pass

    def save_to_json(self, filename: str):
        """
            Зберігає дані про працівників у JSON файл.

            Args:
                filename (str): Ім'я файлу для збереження даних.
        """
        data = [emp.__dict__ for emp in self.employees]
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_from_json(self, filename: str):
        """
            Завантажує дані про працівників з JSON файлу.

            Args:
                filename (str): Ім'я файлу для завантаження даних.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            for emp_data in data:
                employee = EmployeeImplementation(emp_data['last_name'], emp_data['first_name'], emp_data['position'])
                self.employees.append(employee)


class Sale(ABC):
    """
    Абстрактний класс який відображає продаж автомобіля
    """
    def __init__(self, employee: Employee, car: Car, actual_price: float):
        """
        Ініціалізація класу

        :param employee: Екземпляр класу Employee
        :param car: Екземпляр класу Car
        :param actual_price: Фактична ціна продажу автомобіля
        """
        self.employee = employee
        self.car = car
        self.actual_price = actual_price

    def to_dict(self) -> dict:
        """
        Перетворює обєкт Sale у словник
        :return: dict : Словник з даними про продаж
        """
        return {
            "employee": self.employee.__dict__,
            "car": self.car.__dict__,
            "actual_price": self.actual_price
        }


class SalesManager(ABC):
    """
    Абстрактний клас , який представляє співробітника по продажах.
    """
    def __init__(self):
        """Ініціалізація класу"""
        self.sales_records = []

    def add_sale_record(self, sale_record: Sale):
        """
        Додає запис про продаж до журналу
        :param sale_record: Запис про продаж
        """
        for record in self.sales_records:
            if self.is_same_sale(record, sale_record):
                record.actual_price = sale_record.actual_price
                self.save_to_json("sales.json")
                print("Sale record updated successfully.")
                return
        self.sales_records.append(sale_record)
        self.save_to_json("sales.json")

    def is_same_sale(self, record1: Sale, record2: Sale) -> bool:
        """Перевірка на ідентичність запису про продаж."""
        return record1.employee.last_name == record2.employee.last_name \
               and record1.employee.first_name == record2.employee.first_name \
               and record1.car.manufacturer == record2.car.manufacturer \
               and record1.car.model == record2.car.model

    def remove_sale_record(self, sale_record: Sale):
        """
        Видалення запису про продаж з Json файла

        :arg : sale_record: Sale запис про продаж, який потрібно видалити
        """
        self.sales_records.remove(sale_record)
        self.save_to_json("sales.json")

    def display_employee_sales_info(self):
        """
        Відображення інформація про продажі працівників.
        :return:
        """
        print("Employee Sales Information:")
        for record in self.sales_records:
            print(
                f"Employee: {record.employee.last_name} {record.employee.first_name}, Car: {record.car.manufacturer} {record.car.model}, Actual Price: {record.actual_price}")

    def display_car_info(self, car_inventory: CarInventory = None):
        """
        Відображення інформація про автомобілі на складах.
        :param car_inventory:
        :return:
        """
        if car_inventory is None:
            print("No car inventory provided.")
            return
        print("Car Information:")
        for car in car_inventory.cars:
            print(
                f"Manufacturer: {car.manufacturer}, Model: {car.model}, Year: {car.year}, Cost Price: {car.cost_price}, Selling Price: {car.selling_price}")

    def calculate_profit(self) -> float:
        """
        Обчислює загальний прибуток від продажів.
        :return:
         float: Загальний прибуток
        """
        profit = 0
        for record in self.sales_records:
            profit += record.actual_price - record.car.cost_price
        return profit

    def display_sales_info(self):
        """
        Відображає інформацію про всі продажі
        :return:
        """
        print("Sales Information:")
        for record in self.sales_records:
            print(
                f"Car: {record.car.manufacturer} {record.car.model}, Sold by: {record.employee.last_name} {record.employee.first_name}, Actual Price: {record.actual_price}")

    def save_to_json(self, filename: str):
        """
        Зберігання інформації у JSON файл.
        :param filename:
        :return:
        """
        data = [sale_record.to_dict() for sale_record in self.sales_records]
        with open(filename, 'w') as file:
            json.dump(data, file)


# Реалізація класів

class CarImplementation(Car):
    """
        Клас, що реалізує конкретну реалізацію автомобіля.
    """
    def display_details(self):
        """
            Відображає деталі автомобіля.
        """
        print(
            f"Manufacturer: {self.manufacturer}, Year: {self.year}, Model: {self.model}, Cost Price: {self.cost_price}, Selling Price: {self.selling_price}")

    def sell(self):
        """
            Продаж автомобіля.

            Помічає автомобіль як проданий, оновлює кількість автомобілів у наявності та записує зміни у JSON файл.
        """
        if not self.sold and self.quantity_left > 0:
            self.sold = True
            self.quantity -= 1
            self.quantity_left -= 1
            print("Car sold successfully.")
            self.update_json()
        elif self.quantity_left == 0:
            print("This car is out of stock.")
        else:
            print("This car has already been sold.")


class CarInventoryImplementation(CarInventory):
    """
        Клас, що реалізує конкретну реалізацію інвентаря автомобілів.
    """
    def get_car(self, index: int) -> Car:
        """
            Повертає автомобіль з інвентаря за вказаним індексом.

            Args:
                index (int): Індекс автомобіля.

            Returns:
                    Car: Автомобіль з інвентаря.
        """
        return self.cars[index]

    def load_from_json(self, filename: str):
        """
            Завантажує дані про автомобілі з JSON файлу у інвентар.

            Args:
                filename (str): Ім'я файлу для завантаження даних.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            for car_data in data:
                quantity = car_data.get('quantity', 1)
                quantity_left = car_data.get('quantity_left', 1)
                car = CarImplementation(car_data['manufacturer'], car_data['year'], car_data['model'],
                                        car_data['cost_price'], car_data['selling_price'], quantity, quantity_left)
                self.cars.append(car)


class EmployeeImplementation(Employee):
    """
        Клас, що реалізує конкретну реалізацію працівника.
    """
    def display_details(self):
        """
            Відображає деталі працівника.
        """
        print(f"Employee: {self.last_name} {self.first_name}, Position: {self.position}")


class EmployeeRegistryImplementation(EmployeeRegistry):
    """
        Клас, що реалізує конкретну реалізацію реєстру працівників.
    """
    def get_employee(self, index: int):
        """
             Повертає працівника з реєстру за вказаним індексом.
        """
        return self.employees[index]

    def save_to_json(self, filename: str):
        """
            Зберігає дані про працівників у JSON файл.

            Args:
                filename (str): Ім'я файлу для збереження даних.
        """
        data = [emp.__dict__ for emp in self.employees]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename: str):
        """
            Завантажує дані про працівників з JSON файлу у реєстр.

            Args:
                filename (str): Ім'я файлу для завантаження даних.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            for emp_data in data:
                employee = EmployeeImplementation(emp_data['last_name'], emp_data['first_name'], emp_data['position'])
                self.employees.append(employee)


class SalesManagerImplementation(SalesManager):
    """
        Клас, що реалізує конкретну реалізацію менеджера продажів.
    """
    def add_sale_record(self, sale_record: Sale):
        """
            Додає запис про продаж до журналу.

            Args:
                sale_record (Sale): Запис про продаж.
        """
        for record in self.sales_records:
            if self.is_same_sale(record, sale_record):
                record.actual_price = sale_record.actual_price
                self.save_to_json("sales.json")
                print("Sale record updated successfully.")
                return
        self.sales_records.append(sale_record)
        self.save_to_json("sales.json")

    def is_same_sale(self, record1: Sale, record2: Sale) -> bool:
        """
                Перевіряє, чи є два записи про продаж ідентичними.
        """
        return record1.employee.last_name == record2.employee.last_name \
               and record1.employee.first_name == record2.employee.first_name \
               and record1.car.manufacturer == record2.car.manufacturer \
               and record1.car.model == record2.car.model

    def remove_sale_record(self, sale_record: Sale):
        """
                Видаляє запис про продаж з журналу.
        """
        self.sales_records.remove(sale_record)
        self.save_to_json("sales.json")

    def display_employee_sales_info(self):
        """
            Відображає інформацію про продажі працівників.
        """
        print("Employee Sales Information:")
        for record in self.sales_records:
            print(
                f"Employee: {record.employee.last_name} {record.employee.first_name}, Car: {record.car.manufacturer} {record.car.model}, Actual Price: {record.actual_price}")

    def display_car_info(self, car_inventory: CarInventory = None):
        """
            Відображає інформацію про автомобілі у інвентарі.
        """
        if car_inventory is None:
            print("No car inventory provided.")
            return
        print("Car Information:")
        for car in car_inventory.cars:
            print(
                f"Manufacturer: {car.manufacturer}, Model: {car.model}, Year: {car.year}, Cost Price: {car.cost_price}, Selling Price: {car.selling_price}")

    def calculate_profit(self):
        """
            Обчислює загальний прибуток від продажів.

            Returns:
                    float: Загальний прибуток.
        """
        profit = 0
        for record in self.sales_records:
            profit += record.actual_price - record.car.cost_price
        return profit

    def display_sales_info(self):
        """
            Відображає інформацію про всі продажі.
        """
        print("Sales Information:")
        for record in self.sales_records:
            print(
                f"Car: {record.car.manufacturer} {record.car.model}, Sold by: {record.employee.last_name} {record.employee.first_name}, Actual Price: {record.actual_price}")

    def save_to_json(self, filename: str):
        """
            Зберігає дані про продажі у JSON файл.
        """
        data = [sale_record.to_dict() for sale_record in self.sales_records]
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)


def main():
    """
    Основна функція програми, для взаємодії з користувачами
    """
    car_inventory = CarInventoryImplementation()
    employee_registry = EmployeeRegistryImplementation()
    sales_manager = SalesManagerImplementation()

    employee_registry.load_from_json("employees.json")
    car_inventory.load_from_json("cars.json")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            for employee in employee_registry.employees:
                employee.display_details()
        elif choice == '2':
            for car in car_inventory.cars:
                car.display_details()
        elif choice == '3':
            sales_manager.display_employee_sales_info()
        elif choice == '4':
            add_employee(employee_registry)
        elif choice == '5':
            add_car(car_inventory)
        elif choice == '6':
            add_sale(sales_manager, employee_registry, car_inventory)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def display_menu():
    """
    Відображення головного меню.
    """
    print("\nMenu:")
    print("1. Show employees")
    print("2. Show remaining cars")
    print("3. Show sales by employees")
    print("4. Add an employee")
    print("5. Add a car")
    print("6. Add a sale")
    print("7. Exit")


def add_employee(employee_registry: EmployeeRegistry):
    """
    Додавання нового працівника
    :param employee_registry: EmployeeRegistry:  Реєстр працівників
    """
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
    """
    Додавання нового автомобіля до інвертаря.
    :param car_inventory: CarInventory: Склад Автомобілів.
    """
    while True:
        try:
            manufacturer = input("Enter car manufacturer: ")
            year = int(input("Enter car year: "))
            model = input("Enter car model: ")
            cost_price = float(input("Enter car cost price: "))
            selling_price = float(input("Enter car selling price: "))
            quantity = int(input("Enter quantity: "))
            new_car = CarImplementation(manufacturer, year, model, cost_price, selling_price, quantity, quantity)
            car_inventory.add_car(new_car)
            print("Car added successfully.")
            break
        except Exception as e:
            print(f"Error: {e}")
            choice = input("Do you want to try again? (yes/no): ")
            if choice.lower() != 'yes':
                break


def add_sale(sales_manager: SalesManager, employee_registry: EmployeeRegistry, car_inventory: CarInventory):
    """
    Додавання запису про продаж.

    :param sales_manager:  SalesManager: Співробітник по продажу.
    :param employee_registry: EmployeeRegistry: Реєстр працівників.
    :param car_inventory: CarInventory: Інвентар автомобілів.
    """
    while True:
        try:
            print("Add a sale:")
            employee_name = input("Enter employee's last name or first name: ")
            car_manufacturer = input("Enter car manufacturer: ")
            car_model = input("Enter car model: ")
            actual_price = float(input("Enter actual price of the car sold: "))

            employee = next((emp for emp in employee_registry.employees if
                             emp.last_name == employee_name or emp.first_name == employee_name), None)
            car = next((car for car in car_inventory.cars if
                        car.manufacturer == car_manufacturer and car.model == car_model and car.quantity_left > 0 and not car.is_sold()),
                       None)

            if employee is None:
                raise ValueError("Employee not found.")
            if car is None:
                raise ValueError("Car not found, already sold, or out of stock.")

            new_sale = Sale(employee, car, actual_price)
            sales_manager.add_sale_record(new_sale)
            car.sell()
            print("Sale added successfully.")
            break
        except Exception as e:
            print(f"Error: {e}")
            choice = input("Do you want to try again? (yes/no): ")
            if choice.lower() != 'yes':
                break


if __name__ == "__main__":
    main()
