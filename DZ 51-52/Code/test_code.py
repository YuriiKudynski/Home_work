from code import BankAccount

user1 = BankAccount("Mikky Ruk", "31567", 1300, "UAH")
user2 = BankAccount("Alice Parker", "34565", 1000, "USD")
user3 = BankAccount("Nikky Mick", "62162", 800, "EUR")
user4 = BankAccount("Alicon New", "21352", 1000, "JPY")
user4.save_data()
user4.remove_account("21352")
print(*BankAccount.accounts)

user1.save_data()
user2.save_data()
user3.save_data()

user1.deposit(500)
user1.save_data()

user1.load_data()
user1.display_account_info()



user1.change_owner_name("Matiaz Kintry")
print()
user1.transfer_funds(user2, 500)
print()
user2.transfer_funds(user3, 50)
print()
user3.transfer_funds(user1, 20)
print()
user1.transfer_funds(user3, 20000)
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

print(BankAccount.check_account_number(user1.account_number))

