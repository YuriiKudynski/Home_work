from code import BankAccount


class NewBankAccount(BankAccount):

    def __init__(self, owner_name, account_number, balance, currency, max_limit, max_count_transactions):
        super().__init__(owner_name, account_number, balance, currency)
        self.max_limit = max_limit
        self.max_count_transactions = max_count_transactions
        self.current_transaction = 0

    def withdraw(self, amount):
        if self.current_transaction >= self.max_count_transactions:
            print("Перевищено кількість операцій зняття")
            return

        if amount > self.max_limit:
            print("Перевищено максимальний ліміт зняття")
            return

        self.current_transaction += 1
        super().withdraw(amount)

    def transfer_funds(self, target_account, amount):
        if self.current_transaction >= self.max_count_transactions:
            print("Перевищено кількість операцій переказу")
            return

        if amount > self.max_limit:
            print("Перевищено максимальний ліміт переказу")
            return

        self.current_transaction += 1
        super().transfer_funds(target_account, amount)

    def add_procent(self, procent):
        new_amount = self._balance.amount * (procent / 100)
        self._balance.amount += new_amount
        print(f"Нараховано відсотки: {new_amount:.2f} {self._balance.currency}")


user4 = NewBankAccount("Alice Parker", "13529", 1000,
                       "EUR", 200, 3)
user5 = NewBankAccount("Jon Wick", "77777", 1000,
                       "EUR", 300, 3)
user6 = NewBankAccount("Den Nova", "85112", 1000,
                       "EUR", 300, 3)

try:
    user4.add_procent(15)
    user4.display_account_info()
    # user6.withdraw(10)
    # user6.withdraw(10)
    # user6.withdraw(10)
    # user6.withdraw(10)
    # user4.transfer_funds(user5, 100)
    # user4.transfer_funds(user5, 100)
    # user4.transfer_funds(user5, 100)
    # user4.transfer_funds(user5, 100)

except Exception as e:
    print(e)
