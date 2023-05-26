# from .account import Account
from .transaction import Transaction


class Client:
    def __init__(self, address: str, name: str):
        self.address = address
        self.accounts = []
        self.name = name

    def create_account(self, account):
        self.accounts.append(account)

    def transaction(self, account, transaction_type: Transaction):
        transaction_type.register(account)
