from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employees(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employees:")
        for e in self.employees:
            print(e.fname, e.lname)
        print("------------------------------------")

    def pay_employees(self):
        print("Paying Employees:")
        for e in self.employees:
            print("Paycheck for", e.fname, e.lname)
            print(f"Amount: ${e.calculate_paycheck():,.2f}")

def main():
    my_company = Company()

    employee1 = SalaryEmployee("Stevenson", "Yan", 150000)
    my_company.add_employees(employee1)
    employee2 = HourlyEmployee("Linda", "Han", 40, 32)
    my_company.add_employees(employee2)
    employee3 = CommissionEmployee("Joe", "Mama", 150000, 10, 100)
    my_company.add_employees(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()