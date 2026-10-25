""""
Q1. Bank Account
Model a BankAccount with deposit, withdraw, and balance. Withdrawals can’t overdraw. Keep the balance from being modified directly.

Tests: encapsulation, @property, custom exceptions
Twist: add a SavingsAccount with a monthly withdrawal limit. What changes?
"""


class MonthlyLimitExceededError(Exception):
    pass


class BankAccount:

    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount
        return self.__balance


class SavingsAccount(BankAccount):

    WITHDRAWAL_LIMIT = 3

    def __init__(self, balance=0):
        super().__init__(balance)
        self.__withdrawal_count = 0

    def withdraw(self, amount):
        if self.__withdrawal_count >= self.WITHDRAWAL_LIMIT:
            raise MonthlyLimitExceededError(
                "Monthly withdrawal limit exceeded"
            )

        result = super().withdraw(amount)

        self.__withdrawal_count += 1

        return result


# Testing
account = SavingsAccount(1000)

print(account.withdraw(100))  # 900
print(account.withdraw(100))  # 800
print(account.withdraw(100))  # 700

# Fourth withdrawal raises MonthlyLimitExceededError
print(account.withdraw(100))