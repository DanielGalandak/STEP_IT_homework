# 11_bank_account.py

class Account:
    def __init__(self, account_number: int, account_owner: str, balance: int):
            self.account_number = account_number
            self.acount_owner = account_owner
            self.balance = balance

    def withdraw(self, amount: int):
          self.balance -= amount
    
    def deposit(self, amount: int):
          self.balance += amount
    
    def display_balance(self):
          print(self.balance)
    

jirka = Account(123456789, 'Jirka Sirka', 78932)

jirka.withdraw(32)
jirka.display_balance()
jirka.deposit(100)
jirka.display_balance()