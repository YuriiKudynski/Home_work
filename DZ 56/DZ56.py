from dz54 import NewBankAccount
from code import BankAccount


class UpBankAccount(NewBankAccount):

    def __eq__(self, other):
        """Return True if self-balance currency and self-balance amount are equal. Else False"""
        if isinstance(other, UpBankAccount):
            return (self._balance.currency == other._balance.currency and
                    self._balance.amount == other._balance.amount)
        return False

    def __lt__(self, other):
        """Return True if self-balance amount in UAH are lower than other-balance amount"""
        if isinstance(other, UpBankAccount):
            self_balance_uah = self._balance.amount * BankAccount._BankAccount__exchange_rate.get(
                self._balance.currency)
            other_balance_uah = other._balance.amount * BankAccount._BankAccount__exchange_rate.get(
                other._balance.currency)
            return self_balance_uah < other_balance_uah

    def __bool__(self):
        """Return True if self-balance not zero"""
        return self._balance.amount > 0

    def __float__(self):
        """Return float value self-balance amount"""
        return float(self._balance.amount)

    def __add__(self, numb):
        """Add amount to balance without new function with equal id. Use (user + (int))"""
        if isinstance(numb, int):
            self._balance.amount += numb
        return self._balance.amount

    def __sub__(self, numb):
        """Sub amount from balance without new function wit equal id. Use (user - (-int))"""
        if isinstance(numb, int):
            self._balance.amount -= numb
        return self._balance.amount

    def __call__(self, value=0):
        """Self-balance add value if value more zero or self-balance sub value if value lower zero
         If value = 0 show self-balance"""
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
