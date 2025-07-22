import json
from services.company import Company
from services.factory import EmployeeFactory
from core.strategies.bonus_policy import BonusPolicy


class EmployeeManagementMenu:
    def __init__(self):
        with open('config/policies.json') as f:
            policies = json.load(f)["bonus"]
        bonus_policy = BonusPolicy(policies)
        self.company = Company(bonus_policy)

    def run(self):
        while True:
            print("\n--- Employee Management Menu ---")
            print("1. Create employee")
            print("2. Pay employees")
            print("3. Grant vacation / payout")
            print("4. View transaction history")
            print("5. Exit")

            option = input("Select an option: ")

            if option == "1":
                self.create_employee()
            elif option == "2":
                self.company.pay_all()
            elif option == "3":
                self.request_vacation()
            elif option == "4":
                self.company.view_transaction_history()
            elif option == "5":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid option.")

    def create_employee(self):
        emp_type = input("Employee type (salaried/hourly/intern/freelancer): ").lower()
        name = input("Employee name: ")
        role = input("Role (intern, manager, vice_president, other): ").lower()
        data = {"type": emp_type, "name": name, "role": role}

        if emp_type == "salaried":
            data["monthly_salary"] = float(input("Monthly salary: "))
        elif emp_type == "hourly":
            data["hourly_rate"] = float(input("Hourly rate: "))
            data["hours_worked"] = int(input("Hours worked: "))
        elif emp_type == "freelancer":
            data["projects"] = []
            while True:
                project_name = input("Project name (or type 'exit'): ")
                if project_name == "exit":
                    break
                amount = float(input("Project amount: "))
                data["projects"].append({"name": project_name, "amount": amount})

        employee = EmployeeFactory.create_employee(data)
        self.company.add_employee(employee)
        print(f"\nEmployee {employee.name} created successfully.")

    def request_vacation(self):
        if not self.company.employees:
            print("No employees registered.")
            return

        print("\nSelect employee:")
        for idx, emp in enumerate(self.company.employees):
            print(f"{idx}. {emp.name} ({emp.role}) - {emp.vacation_days} vacation days remaining")

        try:
            index = int(input("Employee number: "))
            employee = self.company.employees[index]
            days_requested = int(input("Days requested: "))
            payout = input("Request payout instead of vacation? (y/n): ").lower() == "y"

            result = employee.request_vacation(days_requested, payout)
            print(f"\n✅ {result}")

        except Exception as e:
            print(f"⚠️ Error: {e}")

    def view_transaction_history(self):
        self.company.view_transaction_history()
