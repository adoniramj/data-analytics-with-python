class Payroll:
    def print_payroll(self, employees):
        print("Payroll results")
        print("================")
        for employee in employees:
            print("The salary of employee: {} with id:{} is:".format(employee.name, employee.id))
            print("Amount: {}".format(employee.calculate_pay()))
            print("-------------------------------------------------------------------------------")
        print("End of report")
            