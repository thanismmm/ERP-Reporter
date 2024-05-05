class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

class Manager(Employee):  # Inherits from Employee
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department


class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department  # Association relationship

dept = Department("Finance")
emp = Employee("John Doe", dept)


class DataIngestionContext:
    def __init__(self):
        self.strategy = None  # DataIngestionStrategy is part of DataIngestionContext

    def set_strategy(self, strategy):
        self.strategy = strategy

    def ingest_data(self, file_path):
        return self.strategy.ingest_data(file_path)

class Project:
    def __init__(self, name):
        self.name = name
        self.members = []  # Team members can exist independently of the project

class Employee:
    def __init__(self, name):
        self.name = name

project = Project("AI Development")
emp1 = Employee("Alice")
emp2 = Employee("Bob")

project.members.append(emp1)
project.members.append(emp2)
