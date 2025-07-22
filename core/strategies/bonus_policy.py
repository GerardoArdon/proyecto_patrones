class BonusPolicy:
    def __init__(self, policies):
        self.policies = policies

    def get_bonus(self, employee):
        if employee.__class__.__name__ == "SalariedEmployee":
            return employee.monthly_salary * self.policies["salaried_percentage"]
        elif employee.__class__.__name__ == "HourlyEmployee":
            if employee.hours_worked >= self.policies["hourly_threshold"]:
                return self.policies["hourly_bonus_amount"]
        return 0
