from dz54 import NewBankAccount
from code import BankAccount


class UpBankAccount(NewBankAccount):

    def __eq__(self, other):
        if isinstance(other, UpBankAccount):
            return (self._balance.currency == other._balance.currency and
                    self._balance.amount == other._balance.amount)
        return False

    def __lt__(self, other):
        if isinstance(other, UpBankAccount):
            self_balance_uah = self._balance.amount * BankAccount._BankAccount__exchange_rate.get(
                self._balance.currency)
            other_balance_uah = other._balance.amount * BankAccount._BankAccount__exchange_rate.get(
                other._balance.currency)
            return self_balance_uah < other_balance_uah

    def __bool__(self):
        return self._balance.amount > 0

    def __float__(self):
        return float(self._balance.amount)

    def __add__(self, numb):
        if isinstance(numb, int):
            self._balance.amount += numb
        return self._balance.amount

    def __sub__(self, numb):
        if isinstance(numb, int):
            self._balance.amount -= numb
        return self._balance.amount

    def __call__(self, value=0):
        if value < 0:
            self._balance.amount -= value
            print(f"From balance sub {value}")
        elif value > 0:
            self._balance.amount += value
            print(f"To balance add {value}")
        else:
            print(f"Balance: {self._balance.amount}")


user7 = UpBankAccount("Kori", "12345",
                      1000, "UAH", 300, 3)
user8 = UpBankAccount("Jami", "12351",
                      150, "USD", 500, 5)
user9 = UpBankAccount("Havi", "12612",
                      2000, "UAH", 500, 5)


print(user7)
user7(10)
user7(-20)
user7(0)
