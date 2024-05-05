import pandas as pd
from abc import ABC, abstractmethod

# Abstract Base Class for handling data
class DataHandler(ABC):
    
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    @abstractmethod
    def load_data(self):
        pass

    def display_data(self):
        print("Displaying the first few rows of the dataset:")
        print(self.data.head())

# Concrete implementation for CSV data
class CSVDataHandler(DataHandler):
    
    def load_data(self):
        self.data = pd.read_csv(self.filename)
        print("Data loaded successfully.")

# Usage
file_path = 'Financials.csv'  # Replace with the actual path to your Financials.csv
data_handler = CSVDataHandler(file_path)
data_handler.load_data()
data_handler.display_data()
