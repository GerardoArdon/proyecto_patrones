from abc import ABC, abstractmethod

class VacationPolicy(ABC):
    @abstractmethod
    def request_vacation(self, employee, days_requested, payout):
        pass


class InternVacationPolicy(VacationPolicy):
    def request_vacation(self, employee, days_requested, payout):
        raise PermissionError("Los pasantes no pueden solicitar vacaciones ni payout.")


class ManagerVacationPolicy(VacationPolicy):
    def request_vacation(self, employee, days_requested, payout):
        if payout:
            if days_requested > 10:
                raise ValueError("El payout no puede exceder los 10 días.")
            if employee.vacation_days < days_requested:
                raise ValueError("No tiene días suficientes para solicitar ese payout.")
            employee.vacation_days -= days_requested
            return f"Payout exitoso de {days_requested} días."
        else:
            if employee.vacation_days < days_requested:
                raise ValueError("No tiene suficientes días disponibles.")
            employee.vacation_days -= days_requested
            return f"Vacaciones aprobadas por {days_requested} días."


class VicePresidentVacationPolicy(VacationPolicy):
    def request_vacation(self, employee, days_requested, payout):
        if payout:
            raise PermissionError("Los vicepresidentes no tienen payout, solo vacaciones.")
        if days_requested > 5:
            raise ValueError("Máximo 5 días por solicitud.")
        return f"Vacaciones ilimitadas aprobadas por {days_requested} días."


class DefaultVacationPolicy(VacationPolicy):
    def request_vacation(self, employee, days_requested, payout):
        if payout:
            if employee.vacation_days < days_requested:
                raise ValueError("No tiene días suficientes para solicitar payout.")
            employee.vacation_days -= days_requested
            return f"Payout exitoso de {days_requested} días."
        else:
            if employee.vacation_days < days_requested:
                raise ValueError("No tiene días suficientes para vacaciones.")
            employee.vacation_days -= days_requested
            return f"Vacaciones aprobadas por {days_requested} días."
