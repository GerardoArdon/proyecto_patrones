from abc import ABC, abstractmethod

class PayStrategy(ABC):
    @abstractmethod
    def calculate_pay(self, employee):
        pass
