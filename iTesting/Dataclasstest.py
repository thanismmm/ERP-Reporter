import pytest
import pandas as pd
import sys
sys.path.append('ERP Reporter\DataClasses.py')
from DataClasses import Financial, HR, Purchase, Sales_Data, FinancialAnalysis, HRAnalysis, PurchaseAnalysis, SalesDataAnalysis, DataProcessor, dataset_has_columns


# Test DataSet subclasses initialization
@pytest.mark.parametrize("class_type, expected_name", [
    (Financial, "Financial"),
    (HR, "HR"),
    (Purchase, "Purchase"),
    (Sales_Data, "Sales_Data"),
])
def test_dataset_initialization(class_type, expected_name):
    dataset_instance = class_type()
    assert str(dataset_instance) == f"{expected_name} DataSet"

# Test DataProcessStrategy concrete classes
@pytest.mark.parametrize("strategy, data, expected_output", [
    (FinancialAnalysis(), pd.DataFrame({'column': [1, 2, 3]}), "Processing financial data..."),
    (HRAnalysis(), pd.DataFrame({'column': [1, 2, 3]}), "Processing HR data..."),
    (PurchaseAnalysis(), pd.DataFrame({'column': [1, 2, 3]}), "Processing purchase data..."),
    (SalesDataAnalysis(), pd.DataFrame({'column': [1, 2, 3]}), "Processing sales data..."),
])
def test_process_data(capsys, strategy, data, expected_output):
    processor = DataProcessor(strategy)
    processor.execute(data)
    captured = capsys.readouterr()  # Captures print output
    assert expected_output in captured.out

# Test utility function
def test_dataset_has_columns():
    df = pd.DataFrame({
        'column1': [1, 2, 3],
        'column2': [4, 5, 6]
    })
    assert dataset_has_columns(df, ['column1', 'column2']) == True
    assert dataset_has_columns(df, ['column1', 'column3']) == False

