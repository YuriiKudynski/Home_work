import requests

class Money:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount} - {self.currency}"


class BankAccount:
    accounts = []
    __exchange_rate = []

    def __init__(self, owner_name, account_number, balance, currency):
        self.owner_name = owner_name
        self.__account_number = account_number
        self._balance = Money(balance, currency)
        if self.__account_number in [acc.__account_number for acc in BankAccount.accounts]:
            print("Рахунок із таким номером вже існує!")
        else:
            self.__class__.accounts.append(self)

    def __str__(self):
        return f"Account: {self.__account_number}"

    def deposit(self, amount):
        self._balance.amount += amount
        print(f"До рахунку {self.__account_number} додано {amount}")

    def withdraw(self, amount):
        if amount < self._balance.amount:
            self._balance.amount -= amount
            print(f"З рахунку {self.__account_number} знято {amount}")
        else:
            print(f"Не достатньо коштів на рахунку {self.__account_number}")

    def change_owner_name(self, new_name):
        self.owner_name = new_name
        print(f"Імя власника рахунку змінено на {new_name}!")

    def display_account_info(self):
        print(f"\nOwner name: {self.owner_name}"
              f"\nAccount number: {self.__account_number}"
              f"\nBalance: {self._balance.amount} {self._balance.currency}")

    def transfer(self, another_acc, amount):
        if self._balance.currency != another_acc._balance.currency:
            print("\nУ рахунків різні валюти!")
        else:
            if amount < self._balance.amount:
                self._balance.amount -= amount
                another_acc._balance.amount += amount
                print(f"Кошти переслані з рахунку {self.__account_number} на {another_acc}")
            else:
                print(f"Не достатньо коштів на рахунку {self.__account_number}")

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

