from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
from core.transaction import TransactionLog

@dataclass
class Employee(ABC):
    name: str
    role: str
    vacation_days: int = 25
    transactions: List[TransactionLog] = field(default_factory=list)
    vacation_policy = None  # Política inyectada dinámicamente

    @abstractmethod
    def calculate_payment(self, bonus_policy) -> float:
        pass

    def register_transaction(self, transaction: TransactionLog):
        self.transactions.append(transaction)

    def request_vacation(self, days_requested, payout):
        if not self.vacation_policy:
            raise Exception("No hay política de vacaciones asignada.")
        result = self.vacation_policy.request_vacation(self, days_requested, payout)
        transaction_type = "Payout" if payout else "Vacaciones"
        self.register_transaction(TransactionLog(transaction_type, days_requested, result))
        return result


@dataclass
class SalariedEmployee(Employee):
    monthly_salary: float = 5000

    def calculate_payment(self, bonus_policy) -> float:
        bonus = bonus_policy.get_bonus(self)
        return self.monthly_salary + bonus


@dataclass
class HourlyEmployee(Employee):
    hourly_rate: float = 50
    hours_worked: int = 0

    def calculate_payment(self, bonus_policy) -> float:
        base = self.hourly_rate * self.hours_worked
        bonus = bonus_policy.get_bonus(self)
        return base + bonus


@dataclass
class Intern(Employee):
    def calculate_payment(self, bonus_policy) -> float:
        return 0


@dataclass
class Freelancer(Employee):
    projects: List[dict] = field(default_factory=list)

    def calculate_payment(self, bonus_policy) -> float:
        return sum(p["amount"] for p in self.projects)
