from .account import Account
from .client import Client
from .withdraw import Withdraw


class CurrentAccount(Account):
    def __init__(self, account_number: int, client: Client, limit=3, limit_amount=500):
        super().__init__(account_number, client)
        self.limit = limit
        self.limit_amount = limit_amount

    def withdraw(self, value: float) -> bool:
        amount_withdraw = len(
            [
                transaction
                for transaction in self.historical.transaction
                if transaction["tipo"] == Withdraw.__name__
            ]
        )
        if amount_withdraw >= self.limit:
            print("\n Operação falhou! Número máximo de saques excedido. \n")
        elif value > self.limit_amount:
            print(
                f"\n Operação falhou! O valor do saque excede o limite de R$ {self.limit_amount}. \n"
            )
        else:
            return super().withdraw(value)
        return False

    def __str__(self):
        return f"""\
                 Agência:\t{self.agency}
                 C/C:\t\t{self.account_number}
                 Titular:\t{self.client.name}
             """
