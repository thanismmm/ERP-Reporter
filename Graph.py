import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def panda_data_frame(data):
    data['Date'] = pd.to_datetime(data['Date'])
    return data

def monthly_sales_analysis(data):
    data['year_month'] = data['Date'].dt.to_period('M')
    grouped_data = data.groupby(['Country', 'year_month']).agg({'Units Sold': 'sum', 'Sales': 'sum'}).reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    for label, df in grouped_data.groupby('Country'):
        ax.plot(df['year_month'].dt.to_timestamp(), df['Sales'], label=label)
    ax.set_title('Monthly Sales by Country')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.legend()
    ax.grid(True)
    return fig

def weekly_sales_analysis(data):
    data['week_number'] = data['Date'].dt.isocalendar().week
    weekly_data = data.groupby(['week_number', 'Country']).agg({'Units Sold': 'sum', 'Sales': 'sum'}).reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    for label, df in weekly_data.groupby('Country'):
        ax.plot(df['week_number'], df['Sales'], label=label)
    ax.set_title('Weekly Sales by Country')
    ax.set_xlabel('Week Number')
    ax.set_ylabel('Sales')
    ax.legend()
    ax.grid(True)
    return fig

def price_analysis(data):
    price_stats = data.groupby('Product').agg({'Sales': ['mean', 'sum'], 'Units Sold': 'sum'}).reset_index()
    price_stats.columns = ['Product', 'Average Sales', 'Total Sales', 'Total Units Sold']
    fig, ax = plt.subplots()
    price_stats.plot(x='Product', y='Average Sales', kind='bar', title='Average Sales by Product', ax=ax)
    return fig

@st.cache_data
def load_data():
    return pd.read_csv('data/Financial.csv')


