import pandas as pd
from abc import ABC, abstractmethod

class DataIngestionStrategy(ABC):
    @abstractmethod
    def load_data(self, file_path):
        pass

class CSVDataIngestion(DataIngestionStrategy):
    def load_data(self, file_path):
        df = pd.read_csv(file_path)
        # Standardize column names: strip spaces and convert to lower case
        df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
        return df

class DataIngestionContext:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def load_data(self, file_path):
        return self.strategy.load_data(file_path)
