class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

        
class WeeklyPayEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
    
    def calculate_pay(self):
        return self.weekly_salary

    

class CommissionEmployee(WeeklyPayEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
    
    def calculate_pay(self):
        fixed = super().calculate_pay()
        return self.commission + fixed



class HourlyPayEmployee(Employee):
    def __init__(self, id, name, hourly_rate, hours):
        super().__init__(id, name)
        self.hourly_rate = hourly_rate
        self.hours = hours
    
    def calculate_pay(self):
        return self.hourly_rate * self.hours