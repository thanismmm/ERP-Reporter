import pytest
import pandas as pd
from data_processing.data_processor import DataProcessor, AdvancedFilterDataProcessor, DataProcessingContext

# Test for ensuring DataProcessor cannot be instantiated directly
def test_data_processor_cannot_be_instantiated():
    with pytest.raises(TypeError):
        DataProcessor()

# Tests for AdvancedFilterDataProcessor
@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'age': [25, 30, 35, 40],
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'income': [50000, 60000, 70000, 80000]
    })

def test_advanced_filter_data_processor_no_filters(sample_data):
    processor = AdvancedFilterDataProcessor()
    result = processor.process_data(sample_data)
    pd.testing.assert_frame_equal(result, sample_data)

# Tests for DataProcessingContext
def test_data_processing_context(sample_data):
    context = DataProcessingContext()
    processor = AdvancedFilterDataProcessor()
    context.set_processor(processor)
    filter_options = {'name': 'Alice'}
    result = context.process_data(sample_data, filter_options)
    expected_data = pd.DataFrame({
        'age': [25],
        'name': ['Alice'],
        'income': [50000]
    })
    pd.testing.assert_frame_equal(result, expected_data)

