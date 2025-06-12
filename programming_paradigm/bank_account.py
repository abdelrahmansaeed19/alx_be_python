# bank_account.py

class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.__account_balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self) -> None:
        print(f"Current Balance: ${self.__account_balance:.2f}")
