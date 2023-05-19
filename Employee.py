# Write a python program to create a class called "Employee" with attributes for name, companyName and methods to add and remove Employee from a collection.

class Employee:
    def __init__(self, name, company_name):
        self.name = name
        self.company_name = company_name

class EmployeeCollection:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def print_employees(self):
        print("Employees in the collection:")
        for employee in self.employees:
            print("Name:", employee.name)
            print("Company Name:", employee.company_name)
            print()

# Create an instance of the EmployeeCollection class
collection = EmployeeCollection()

# Add employees to the collection
employee1 = Employee("Ganesh Villers", "Excel Company")
employee2 = Employee("Sahil Smith", "Nora Inc.")
collection.add_employee(employee1)
collection.add_employee(employee2)

# Print the employees in the collection
collection.print_employees()

# Remove an employee from the collection
collection.remove_employee(employee2)

# Print the employees in the collection after removal
collection.print_employees()