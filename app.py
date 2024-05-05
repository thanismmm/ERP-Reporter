import streamlit as st
import pandas as pd
from data_ingestion.data_ingestion import CSVDataIngestion, DataIngestionContext
from data_processing.data_processor import AdvancedFilterDataProcessor, DataProcessingContext
from Graph import panda_data_frame, monthly_sales_analysis, weekly_sales_analysis, price_analysis
from DataClasses import dataset_has_columns  # Ensure this function is properly imported


# Initialize data ingestion and processing contexts
ingestion_context = DataIngestionContext()
ingestion_context.set_strategy(CSVDataIngestion())

processing_context = DataProcessingContext()
processing_context.set_processor(AdvancedFilterDataProcessor())

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://w0.peakpx.com/wallpaper/78/502/HD-wallpaper-premium-business-hand-worker-holding-business-analytics-big-data-analysis-technology-future-concept.jpg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
    object-fit: cover;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


def load_uploaded_data(file):
    return ingestion_context.load_data(file)

def filter_data(data, filter_options):
    for column, value in filter_options.items():
        if value:
            data = data[data[column].astype(str).str.contains(value, case=False, na=False)]
    return data

def prepare_data(data, date_column):
    if date_column in data:
        data[date_column] = pd.to_datetime(data[date_column])
    return data

@st.cache
def load_default_data():
    return pd.read_csv('data/Financial.csv')


# Streamlit UI setup
st.title('ERP System Reporting Tool')

option = st.selectbox(
    'Select Data Option',
    ('Select an option', 'HR', 'Financial', 'Sales', 'Supply Chain', 'Price'), key='Main'
)

# File uploader
uploaded_file = st.file_uploader("Upload your data CSV file", type='csv')

if uploaded_file is not None and option != 'Select an option':
    data = pd.read_csv(uploaded_file)
    unique_columns = {
        'Financial': ['Segment', 'Country'],
        'HR': ['EmpID', 'Employee_Name'],
        'Sales': ['Order ID', 'Product'],
        'Supply Chain': ['Supply ID', 'Quantity'],
        'Price': ['Product ID', 'Price']
    }
    st.write("Data Preview:")
    st.dataframe(data)

    if dataset_has_columns(data, unique_columns[option]):
        st.success("Success: The uploaded file matches the expected dataset type.")
        # You can add code here to show other content or perform further data processing
        # Variables for filter options
        filter_option = st.radio("Select your filtering mode:", ('Filter by Value', 'Filter by Column'))
        filter_options = {}
        all_columns = data.columns

         # Add sorting options in the sidebar
        st.sidebar.header("Sorting Options")
        sort_column = st.sidebar.selectbox(
            "Select column to sort by:",
            data.columns,
            key='sort_column'
        )
        sort_order = st.sidebar.radio(
            "Select sort order:",
            ('Ascending', 'Descending'),
            index=0,
            key='sort_order'
        )
        if st.sidebar.button('Apply Sort'):
            if sort_order == 'Ascending':
                data = data.sort_values(by=sort_column, ascending=True)
            else:
                data = data.sort_values(by=sort_column, ascending=False)
            st.write("Sorted Data:")
            st.dataframe(data)

        # Filtering options and analysis code would go here, unchanged from your previous implementation.

        if filter_option == 'Filter by Value':
            for column in all_columns:
                if st.checkbox(f"Filter by {column}", key=f"check_{column}"):
                    value = st.text_input(f"Enter value for {column}:", key=f"value_{column}")
                    if value:
                        filter_options[column] = value

        elif filter_option == 'Filter by Column':
            selected_columns = [col for col in data.columns if st.checkbox(col, key=col)]

            # Visualize button to apply filters and show filtered data
        if st.button('Apply Filter', key="1"):
            if filter_option == 'Filter by Value' and filter_options:
                filtered_data = filter_data(data, filter_options)
                st.write("Filtered Data:")
                st.dataframe(filtered_data)
            elif filter_option == 'Filter by Column' and selected_columns:
                filtered_data = data[selected_columns]
                st.write("Filtered Data:")
                st.dataframe(filtered_data)

        if option == 'Financial':
            data = pd.read_csv('data/Financial.csv') 
            processed_data = panda_data_frame(data)

            analysis_option = st.selectbox(
                'Select Analysis Type',
                ('Select an option', 'Monthly Sales Analysis', 'Weekly Sales Analysis', 'Price Analysis')
            )

            # Execute the selected analysis
            if analysis_option == 'Monthly Sales Analysis':
                fig = monthly_sales_analysis(processed_data)
                st.pyplot(fig)
            elif analysis_option == 'Weekly Sales Analysis':
                fig_weekly = weekly_sales_analysis(processed_data)
                st.pyplot(fig_weekly)
            elif analysis_option == 'Price Analysis':
                fig_price = price_analysis(processed_data)
                st.pyplot(fig_price)

    else:
        st.error("Invalid: Uploaded file does not match the expected dataset type. Missing required columns.")