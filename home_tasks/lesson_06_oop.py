class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f"Name from Person class: {self.name}"



class Employee(Person):
    def __init__(self, name, salary, rule):
        super().__init__(name)
        self.__salary = salary
        self.__rule = rule

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative value.")
        else:
            self.__salary = salary


    @property
    def rule(self):
        return self.__rule

    @rule.setter
    def rule(self, rule):
        if rule == "":
            raise ValueError("Rule cannot be empty.")
        else:
            self.__rule = rule



employee = Employee("Dvora", 12000, "QA and automation")
print(employee.get_name())

print(f"Salary: {employee.salary}")
print(f"Rule: {employee.rule}")

employee.salary = 15000
employee.rule = "QA"

print("\nAfter update: ")
print(f"New salary: {employee.salary}")
print(f"New rule: {employee.rule}")

try:
    employee.salary = -1000
except ValueError as ve:
    print(f"\nValidation error: {ve}")

