import pandas as pd
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    @abstractmethod
    def process_data(self, data, filter_options=None):
        """Process data based on provided filter options."""
        pass

class AdvancedFilterDataProcessor(DataProcessor):
    def process_data(self, data, filter_options=None):
        """Apply advanced filters dynamically based on the filter_options dict."""
        if filter_options:
            for column, criteria in filter_options.items():
                if isinstance(criteria, list):
                    if 'range' in criteria[0]:
                        data = data[data[column].between(criteria[1], criteria[2])]
                    else:
                        data = data[data[column].isin(criteria)]
                else:
                    data = data[data[column].astype(str).str.contains(criteria)]
        return data

class DataProcessingContext:
    def __init__(self):
        self.processor = None

    def set_processor(self, processor):
        """Set the processing strategy."""
        self.processor = processor

    def process_data(self, data, filter_options=None):
        """Process the data using the selected processor and options."""
        return self.processor.process_data(data, filter_options)
