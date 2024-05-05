import pytest
import pandas as pd
from Graph import panda_data_frame, monthly_sales_analysis, weekly_sales_analysis, price_analysis

# Assuming 'your_module' is the name of the Python file containing your functions.
# Replace 'your_module' with the actual name of your Python file where the functions are defined.

def test_panda_data_frame():
    data = {'Date': ['2022-01-01', '2022-01-02']}
    df = pd.DataFrame(data)
    transformed_df = panda_data_frame(df)
    assert pd.api.types.is_datetime64_any_dtype(transformed_df['Date']), "Date column should be datetime type"

def test_monthly_sales_analysis():
    data = {'Date': ['2022-01-01', '2022-02-01'], 'Country': ['USA', 'USA'], 'Units Sold': [100, 200], 'Sales': [1000, 2000]}
    df = pd.DataFrame(data)
    df = panda_data_frame(df)  # preprocess data
    fig = monthly_sales_analysis(df)
    assert len(fig.axes[0].lines) > 0, "Should have at least one line plot on the axis"

# Assuming the backend and imports are set
def test_weekly_sales_analysis():
    data = {'Date': ['2022-01-01', '2022-01-08'], 'Country': ['USA', 'USA'], 'Units Sold': [100, 200], 'Sales': [1000, 2000]}
    df = pd.DataFrame(data)
    df = panda_data_frame(df)  # preprocess data
    fig = weekly_sales_analysis(df)
    assert len(fig.axes[0].lines) > 0, "Should have at least one line plot on the axis"

def test_price_analysis():
    data = {'Product': ['Widget', 'Gadget'], 'Sales': [1500, 2500], 'Units Sold': [15, 25]}
    df = pd.DataFrame(data)
    fig = price_analysis(df)
    assert 'Bar' in str(fig.axes[0].containers), "Should contain a bar container"
    assert fig.axes[0].get_title() == 'Average Sales by Product', "Title should match"

# Optional: Add more tests as needed to cover other functions or edge cases.
