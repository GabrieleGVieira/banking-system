from datetime import datetime


class Historical:
    def __init__(self):
        self._transaction = []

    @property
    def transaction(self) -> list:
        return self._transaction

    def add_transaction(self, transaction):
        self._transaction.append(
            {
                "tipo": transaction.__class__.__name__,
                "valor": transaction.value,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
