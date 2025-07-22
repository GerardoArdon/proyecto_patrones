from core.models.employee import SalariedEmployee, HourlyEmployee, Intern, Freelancer
from core.strategies.vacation_policy import (
    InternVacationPolicy,
    ManagerVacationPolicy,
    VicePresidentVacationPolicy,
    DefaultVacationPolicy
)

class EmployeeFactory:
    @staticmethod
    def create_employee(data):
        emp_type = data["type"]
        role = data.get("role", "").lower()

        # Crear copia del diccionario y eliminar la clave 'type'
        data_clean = data.copy()
        data_clean.pop("type", None)

        if emp_type == "salaried":
            employee = SalariedEmployee(**data_clean)
        elif emp_type == "hourly":
            employee = HourlyEmployee(**data_clean)
        elif emp_type == "intern":
            employee = Intern(**data_clean)
        elif emp_type == "freelancer":
            employee = Freelancer(**data_clean)
        else:
            raise ValueError("Tipo de empleado inválido.")

        # Asignar política de vacaciones según el rol
        if role == "intern":
            employee.vacation_policy = InternVacationPolicy()
        elif role == "manager":
            employee.vacation_policy = ManagerVacationPolicy()
        elif role == "vice_president":
            employee.vacation_policy = VicePresidentVacationPolicy()
        else:
            employee.vacation_policy = DefaultVacationPolicy()

        return employee
