import json
import os.path

import requests


class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount:.2f} - {self.currency}"


class BankAccount:
    accounts = []
    __exchange_rate = {"UAH": 1}

    @classmethod
    def get_exchange_rate(cls):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        r = requests.get(url)
        data = r.json()
        for item in data:
            currency = item["cc"]
            rate = item["rate"]
            cls.__exchange_rate[currency] = rate

    def __init__(self, owner_name, account_number, balance, currency):
        self.owner_name = owner_name
        self.__account_number = account_number
        self._balance = Money(balance, currency)
        if self.__account_number in [acc.__account_number for acc in BankAccount.accounts]:
            print("Рахунок із таким номером вже існує!")
        else:
            self.__class__.accounts.append(self)
            self.save_data()

    def __str__(self):
        return f"Account: {self.__account_number}"

    def deposit(self, amount):
        self._balance.amount += amount
        print(f"До рахунку {self.__account_number} додано {amount:.2f} {self._balance.currency}")

    def withdraw(self, amount):
        if amount < self._balance.amount:
            self._balance.amount -= amount
            print(f"З рахунку {self.__account_number} знято {amount:.2f} {self._balance.currency} ")
        else:
            print(f"Не достатньо коштів на рахунку {self.__account_number}")

    def change_owner_name(self, new_name):
        self.owner_name = new_name
        print(f"Імя власника рахунку змінено на {new_name}!")
        self.save_data()

    def display_account_info(self):
        print(f"\nOwner name: {self.owner_name}"
              f"\nAccount number: {self.__account_number}"
              f"\nBalance: {self._balance.amount} {self._balance.currency}")

    def _calculate_transfer_amount(self, target_account, amount):
        try:
            rate_self = BankAccount.__exchange_rate.get(self._balance.currency)
            rate_target_acc = BankAccount.__exchange_rate.get(target_account._balance.currency)

            if rate_self is None or rate_target_acc is None:
                raise ValueError("Обмінний курс не визначений для однієї з валют")

            new_amount = (amount * rate_self) / rate_target_acc
            return new_amount
        except Exception as e:
            raise ValueError(f"Помилка при обчисленні обмінного курсу: {e}")

    def transfer_funds(self, target_account, amount):
        self_currency = self._balance.currency

        try:
            if self._balance.amount >= amount:
                new_amount = self._calculate_transfer_amount(target_account, amount)
                self._balance.amount -= amount
                target_account._balance.amount += new_amount

                print(f"Трансфер {amount} {self_currency} відбувся.\n"
                      f"Баланс рахунку {self.__account_number}: {self._balance}\n"
                      f"Баланс рахунку {target_account.__account_number}: {target_account._balance}")
            else:
                print(f"Недостатньо коштів на рахунку {self.__account_number} для трансферу.")
        except ValueError as e:
            print(f"Помилка при обробці трансферу: {e}")
        except Exception as e:
            print(f"Інша помилка при обробці трансферу: {e}")

    @staticmethod
    def check_account_number(account_number):
        return len(str(account_number)) == 5 and str(account_number).isdigit()

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, new_account_number):
        if not BankAccount.check_account_number(new_account_number):
            raise ValueError("Некоректний номер рахунку")
        self.__account_number = new_account_number
        self.save_data()

    @classmethod
    def find_accounts_by_owner(cls, owner_name):
        matching_accounts = []
        for account in cls.accounts:
            if account.owner_name == owner_name:
                matching_accounts.append(account)
        return matching_accounts

    @classmethod
    def get_average_balance(cls):
        total = sum(account._balance.amount for account in cls.accounts)
        average = total / len(cls.accounts)
        return average

    def save_data(self):
        account_filename = os.path.join(os.path.dirname(__file__), "data", f"{self.__account_number}.txt")
        account_data = {
            "owner_name": self.owner_name,
            "balance_amount": self._balance.amount,
            "balance_currency": self._balance.currency
        }

        with open(account_filename, "w") as file:
            json.dump(account_data, file)

    def load_data(self):
        account_name = os.path.join(os.path.dirname(__file__), "data", f"{self.__account_number}.txt")

        if os.path.exists(account_name):
            with open(account_name, "r") as file:
                account_data = json.load(file)
                self.owner_name = account_data["owner_name"]
                self._balance.amount = account_data["balance_amount"]
                self._balance.currency = account_data["balance_currency"]
        else:
            print("Файл не знайдено!")

    @classmethod
    def remove_account(cls, account_number):
        for account in cls.accounts:
            if account.__account_number == account_number:
                cls.accounts.remove(account)

                filename = os.path.join(os.path.dirname(__file__), "data", f"{account_number}.txt")
                if os.path.exists(filename):
                    os.remove(filename)

                print(f"Рахунок {account_number} видалено.")

                break
        else:
            print(f"Рахунок з номером {account_number} не знайдено.")


BankAccount.get_exchange_rate()