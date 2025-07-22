from core.transaction import TransactionLog

class Company:
    def __init__(self, bonus_policy):
        self.employees = []
        self.bonus_policy = bonus_policy

    def add_employee(self, employee):
        self.employees.append(employee)

    def pay_all(self):
        for emp in self.employees:
            amount = emp.calculate_payment(self.bonus_policy)
            emp.register_transaction(TransactionLog(
                "Pago",
                amount,
                "Pago mensual con bonificación aplicada"
            ))
            print(f"{emp.name} ha recibido un pago de ${amount:.2f}")

    def list_by_role(self, role):
        return [e for e in self.employees if e.role == role]

    def view_transaction_history(self):
        for emp in self.employees:
            print(f"\nHistorial de transacciones de {emp.name}:")
            if not emp.transactions:
                print("  Sin transacciones registradas.")
            for t in emp.transactions:
                print(f"  {t.date} | {t.operation} | ${t.amount:.2f} | {t.description}")

    def list_employees(self):
        return self.employees