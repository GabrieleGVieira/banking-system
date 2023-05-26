from .client import Client


class PrivateIndividual(Client):
    def __init__(self, address, name, cpf: int, birthday: str):
        super().__init__(address, name)
        self.cpf = cpf
        self.birthday = birthday
