class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_employees(employees, sorting_parameter):
    if sorting_parameter == "age":
        employees.sort(key=lambda employee: employee.age)
    elif sorting_parameter == "name":
        employees.sort(key=lambda employee: employee.name)
    elif sorting_parameter == "salary":
        employees.sort(key=lambda employee: employee.salary)
    else:
        print("Invalid sorting parameter.")
        return

    return employees

# Create employee objects based on the extracted data
employees = [
    Employee("161E90", "Ramu", 35, 59000),
    Employee("171E22", "Tejas", 30, 82100),
    Employee("171G55", "Abhi", 25, 100000),
    Employee("152K46", "Jaya", 32, 85000)
]

# Get user input for sorting parameter
sorting_parameter = input("Choose sorting parameter (age, name, salary): ").lower()

# Sort and print the employees
sorted_employees = sort_employees(employees, sorting_parameter)

if sorted_employees:
    print("Sorted Employee Data:")
    for employee in sorted_employees:
        print(f"Employee ID: {employee.employee_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")
