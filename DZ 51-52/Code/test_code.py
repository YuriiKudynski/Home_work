from code import BankAccount

user1 = BankAccount("Mikky Ruk", "31567", 200, "USD")
user2 = BankAccount("Alice Parker", "34565", 100, "USD")
user3 = BankAccount("Nikky Mick", "62162", 500, "EUR")

user1.change_owner_name("Matiaz Kintry")

user1.deposit(20)

user1.transfer(user2, 100)
user1.transfer(user3, 1)

print()

user1.display_account_info()
user2.display_account_info()
user3.display_account_info()

print()
current_number = user1.account_number
print(f"Номер рахунку: {current_number}")
user1.account_number = "12621"
print()
print(f"Новий номер рахунку {user1.account_number}")
print()
matching_accounts = BankAccount.find_accounts_by_owner("Alice Parker")
print(*matching_accounts)
print()
average_balance = BankAccount.get_average_balance()
print(f"Середнє значення всіх балансів {average_balance:.2f}")
print()
print(*BankAccount.accounts)
