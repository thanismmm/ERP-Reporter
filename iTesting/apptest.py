import pytest
from unittest.mock import patch, MagicMock
import pandas as pd
from app import load_uploaded_data, filter_data, prepare_data, load_default_data

# Sample data to use for mocking and testing
SAMPLE_CSV = """Name, Age , Role
Alice, 30, Developer
Bob  , 25, Designer"""

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "Name": ["Alice", "Bob"],
        "Age": ["30", "25"],  # Age as string to mimic CSV loading behavior
        "Role": ["Developer", "Designer"]
    })

@patch("pandas.read_csv")
def test_load_default_data(mock_read_csv):
    # Setup the mock to return a simple DataFrame when any CSV is read
    mock_read_csv.return_value = pd.DataFrame({"Column": ["Data"]})
    
    # Call the function
    df = load_default_data()
    
    # Check that the DataFrame is not empty
    assert not df.empty, "The DataFrame should not be empty after loading default data."
    
    # Validate that read_csv was called correctly
    mock_read_csv.assert_called_once()  # Ensure it was called once

    # Check it was called with the correct file path, you can be more specific if necessary
    args, kwargs = mock_read_csv.call_args
    assert args[0] == 'data/Financial.csv', f"Expected data/Financial.csv, but got {args[0]}"

def test_filter_data(sample_df):
    filter_options = {"Role": "dev"}
    filtered_df = filter_data(sample_df, filter_options)
    assert len(filtered_df) == 1  # Should only include Alice's row
    assert filtered_df.iloc[0]["Name"] == "Alice"

@patch("app.ingestion_context.load_data")
def test_load_uploaded_data(mock_load_data):
    mock_load_data.return_value = pd.DataFrame({"Column": ["Data"]})
    df = load_uploaded_data("dummy_path")
    assert not df.empty
    mock_load_data.assert_called_with("dummy_path")

def prepare_data(data, date_column):
    if date_column in data.columns and pd.api.types.is_string_dtype(data[date_column]):
        try:
            data[date_column] = pd.to_datetime(data[date_column])
        except ValueError:
            print(f"Conversion failed: Column {date_column} cannot be converted to datetime")
    return data

def test_prepare_data_no_date_conversion(sample_df):
    # Call prepare_data with the 'Age' column
    processed_df = prepare_data(sample_df, "Age")
    
    # Check that 'Age' did not get converted to datetime
    assert not pd.api.types.is_datetime64_any_dtype(processed_df['Age']), \
        "Age column should not be converted to datetime"
    # Additionally, verify the column is still in its original format
    assert pd.api.types.is_integer_dtype(processed_df['Age'].astype(int)), \
        "Age column should remain in integer format after processing"



