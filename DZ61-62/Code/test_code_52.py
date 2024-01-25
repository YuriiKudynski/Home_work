import unittest
from code import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account1 = BankAccount("Alice", "16123", 100, "UAH")
        self.account2 = BankAccount("John", "51232", 10, "EUR")
        self.account3 = BankAccount("Mia", "81921", 200, "UAH")

    def tearDown(self):
        del self.account1
        del self.account2
        del self.account3

    def test_deposit(self):
        self.account1.deposit(50)
        self.assertEqual(self.account1._balance.amount, 150)

    def test_withdraw(self):
        self.account1.withdraw(10)
        self.assertEqual(self.account1._balance.amount, 90)

    def test_transfer_funds(self):
        self.account1.transfer_funds(self.account3, 20)
        self.assertEqual(self.account1._balance.amount, 80)
        self.assertEqual(self.account3._balance.amount, 220)

    def test_change_owner_name(self):
        self.account1.change_owner_name("Monica")
        self.assertEqual(self.account1.owner_name, "Monica")


if __name__ == "__main__":
    unittest.main()