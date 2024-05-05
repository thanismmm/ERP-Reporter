import pytest
from unittest.mock import Mock, patch
import pandas as pd
from data_ingestion.data_ingestion import DataIngestionContext, CSVDataIngestion

# Sample data for testing
DATA = """Name, Age , ROLE
Alice, 30, Developer
Bob  , 25,Designer """

@pytest.fixture
def csv_file(tmpdir):
    file = tmpdir.join("Financial.csv")
    file.write(DATA)
    return str(file)

def test_csv_data_ingestion(csv_file):
    # Test loading and formatting of CSV files
    csv_loader = CSVDataIngestion()
    df = csv_loader.load_data(csv_file)

    # Ensure dataframe is loaded correctly
    assert not df.empty, "DataFrame should not be empty"
    # Check the columns are correctly formatted
    expected_columns = ['name', 'age', 'role']
    assert all(col in df.columns for col in expected_columns), "Column names should be standardized"

def test_data_ingestion_context_strategy(csv_file):
    # Setup the context and strategy
    context = DataIngestionContext()
    csv_strategy = CSVDataIngestion()
    context.set_strategy(csv_strategy)

    # Mock the load_data method in CSVDataIngestion
    with patch.object(CSVDataIngestion, 'load_data', return_value=pd.DataFrame()) as mocked_method:
        context.load_data(csv_file)
        mocked_method.assert_called_once_with(csv_file)

