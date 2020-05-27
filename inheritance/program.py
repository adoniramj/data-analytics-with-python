import employee
import payroll

emp_a = employee.WeeklyPayEmployee(1, "John Doe", 1234)
emp_b = employee.HourlyPayEmployee(2, "Jane Doe", 34, 40)
emp_c = employee.CommissionEmployee(3, "John Smith", 1000, 550)

report = payroll.Payroll()

report.print_payroll([emp_a, emp_b, emp_c])