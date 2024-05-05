from abc import ABC, abstractmethod
import pandas as pd


class DataSet(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} DataSet"

class Financial(DataSet):
    def __init__(self):
        super().__init__('Financial')

class HR(DataSet):
    def __init__(self):
        super().__init__('HR')

class Purchase(DataSet):
    def __init__(self):
        super().__init__('Purchase')

class Sales_Data(DataSet):
    def __init__(self):
        super().__init__('Sales_Data')

# Strategy pattern interface
class DataProcessStrategy(ABC):
    @abstractmethod
    def process_data(self, data):
        pass

# Concrete strategy classes
class FinancialAnalysis(DataProcessStrategy):
    def process_data(self, data):
        print("Processing financial data...")
        print(data.head())  # Display first few rows

class HRAnalysis(DataProcessStrategy):
    def process_data(self, data):
        print("Processing HR data...")
        print(data.head())

class PurchaseAnalysis(DataProcessStrategy):
    def process_data(self, data):
        print("Processing purchase data...")
        print(data.head())

class SalesDataAnalysis(DataProcessStrategy):
    def process_data(self, data):
        print("Processing sales data...")
        print(data.head())

# Context class to use the strategy
class DataProcessor:
    def __init__(self, strategy: DataProcessStrategy):
        self.strategy = strategy

    def execute(self, data):
        self.strategy.process_data(data)

def dataset_has_columns(df, columns):
    return all(column in df.columns for column in columns)