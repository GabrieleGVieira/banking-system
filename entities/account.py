from .client import Client
from .historical import Historical


class Account:
    def __init__(self, account_number: int, client: Client):
        self._balance = 0
        self._account_number = account_number
        self._agency = "0001"
        self._client = client
        self._historical = Historical()

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def account_number(self) -> int:
        return self._account_number

    @property
    def agency(self) -> str:
        return self._agency

    @property
    def client(self) -> Client:
        return self._client

    @property
    def historical(self) -> Historical:
        return self._historical

    @classmethod
    def new_account(cls, client: Client, account_number: int):
        return cls(account_number, client)

    def deposit(self, value: float) -> bool:
        if value > 0:
            self._balance += value
            print(f"\n Depoósito no valor de R$ {value} realizado com sucesso! \n")
            return True
        else:
            print("\n Falha na operação. Valor inválido! \n")
            return False

    def withdraw(self, value: float) -> bool:
        if value > self.balance:
            print("\n Saldo insuficiente para completar a operação! \n")
        elif value > 0:
            self._balance -= value
            print(f"\n Saque no valor de R$ {value} realizado com sucesso! \n")
            return True
        else:
            print("\n Falha na operação. Valor inválido! \n")
        return False
