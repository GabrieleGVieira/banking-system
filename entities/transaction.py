from abc import ABC, abstractclassmethod, abstractproperty


class Transaction(ABC):
    @property
    @abstractproperty
    def value(self):
        pass

    @abstractclassmethod
    def register(self, account_number):
        pass
