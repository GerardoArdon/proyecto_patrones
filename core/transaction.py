from dataclasses import dataclass
from datetime import datetime

@dataclass
class TransactionLog:
    date: str
    operation: str
    amount: float
    description: str

    def __init__(self, operation, amount, description):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.operation = operation
        self.amount = amount
        self.description = description
