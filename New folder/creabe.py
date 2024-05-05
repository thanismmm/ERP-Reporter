class DataIngestionFactory:
    @staticmethod
    def get_ingestion_strategy(format_type):
        if format_type == "json":
            return JSONDataIngestion()
        elif format_type == "csv":
            # Placeholder for CSV ingestion strategy
            return CSVDataIngestion()
        else:
            raise ValueError("Unknown format")

# Usage
strategy = DataIngestionFactory.get_ingestion_strategy("json")
data = strategy.ingest_data("data.json")


# Assume we have an older version of a data ingestion class that needs to be adapted.
class LegacyDataLoader:
    def load_data(self, filepath):
        print(f"Loading data from {filepath}")

class DataLoaderAdapter(DataIngestionStrategy):
    def __init__(self, legacy_loader):
        self.legacy_loader = legacy_loader

    def ingest_data(self, file_path):
        self.legacy_loader.load_data(file_path)

# Usage
legacy_loader = LegacyDataLoader()
adapter = DataLoaderAdapter(legacy_loader)
adapter.ingest_data("data.json")


class DataProcessingContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_data(self, data):
        return self.strategy.process_data(data)

class SalesDataProcessingStrategy(DataProcess):
    def process_data(self, data):
        # Implement specific sales data processing
        return processed_data

# Usage
strategy = SalesDataProcessingStrategy()
context = DataProcessingContext(strategy)
result = context.process_data(sales_data)


class CSVDataIngestion(DataIngestionStrategy):
    def ingest_data(self, file_path):
        # CSV reading logic here
        return csv_data


context = DataIngestionContext()
context.set_strategy(CSVDataIngestion())
context.ingest_data("Financials.csv")

class HTMLReportStrategy(DataReportingStrategy):
    def generate_report(self, data):
        # generate HTML report
        pass
class DataIngestionContext:
    def __init__(self, strategy: DataIngestionStrategy):
        self.strategy = strategy

    def ingest_data(self, file_path):
        return self.strategy.ingest_data(file_path)


def find_minimum(numbers):
    if not numbers:
        return None
    minimum_value = numbers[0]
    for number in numbers:
        if number < minimum_value:
            minimum_value = number
    return minimum_value

def count_unique_elements(elements):
    unique_elements = set(elements)
    return len(unique_elements)

def sort_and_find_median(values):
    sorted_values = sorted(values)
    mid_index = len(sorted_values) // 2
    return sorted_values[mid_index]


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

def access_element(index, elements):
    try:
        return elements[index]
    except IndexError:
        print("Failed to access the element: index out of range")
        return None

