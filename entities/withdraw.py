from .account import Account
from .transaction import Transaction


class Withdraw(Transaction):
    def __init__(self, value: float):
        self._value = value

    @property
    def value(self) -> float:
        return self._value

    def register(self, account: Account):
        success_transaction = account.withdraw(self.value)
        if success_transaction:
            account.historical.add_transaction(self)
