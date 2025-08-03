from employee import Employee

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

    employee1 = Employee("Stevenson", "Yan", 150000)
    my_company.add_employees(employee1)
    employee2 = Employee("Linda", "Han", 150000)
    my_company.add_employees(employee2)
    employee3 = Employee("Joe", "Mama", 150000)
    my_company.add_employees(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()