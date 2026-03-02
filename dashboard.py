
import streamlit as st
import pandas as pd
import plotly.express as px
# from datetime import datetime
# PS: the df.index is for the DATE in the CSV file. it 


# =================================== 1. CLEAR DATA =================================== I think!

def main():
    filename = 'ticker_data.csv'
    
#import st
    st.set_page_config(layout="wide")
    st.title("📈 S&P 500, Gold & Silver Dashboard")
# import pd
    # Load data
    df = pd.read_csv(filename,index_col=0,parse_dates=True) #converts date col to datetime format.


    # Sidebar date range
    min_date = df.index.min().date()
    max_date = df.index.max().date()
    start_date, end_date = st.sidebar.date_input(
        "Select date range", 
        [min_date, max_date],
        min_value=min_date, 
        max_value=max_date
    )

    # Filter data based on selection
    mask = (df.index >= pd.Timestamp(start_date)) & (df.index <= pd.Timestamp(end_date))
    df_filtred = df.loc[mask]

    # Create tabs
    #  import px
    tab1, tab2, tab3, tab4 =st.tabs(["US S&P 500", "🥇 Gold", "🥈 Silver", "All"])

    with tab1:
        fig = px.line(
            df_filtred,
            x=df_filtred.index,             # show only date in CSV file
            y='Close_^GSPC',                # show only 'Close_^GSPC' column
            title='S&P - closing price',
            labels={'value': "Price (USD)", 'Date': 'year'}
        )
        # show()
        st.plotly_chart(fig, use_container_width=True)

    with tab2: # Gold may have NaNs, Plotly will skip them
        fig = px.line(
            df_filtred,
            x=df_filtred.index,
            y='Close_GC=F',
            title='GOLD - closing prices',
            labels={'value':"Price (USD)",'Date': "year"}
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        fig = px.line(
            df_filtred,
            x=df_filtred.index,
            y='Close_SI=F',
            title='SILVER - closing price',
            labels={'value':"Price (USD)", 'Date': "year"}
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab4: 
        fig = px.line(
            df_filtred,
            title='All the aviable data',
            x=df_filtred.index,
            y=['Close_^GSPC', 'Close_GC=F', 'Close_SI=F'],
            labels={'value':"Price (USD)",'Date':"year"}
        )
        st.plotly_chart(fig, use_container_width=True)



# I've to add an inflation chart, cuz I see a jump in gold prices, wich match the S&P for the last 5years. "is it because inflation?, maybe the AI revo?"
#  find I way to make tabs code shorter. the only change I do is the y=col_name and title=title

if __name__ == "__main__":
    main()

    # def get_info()
    #   print (df.head())           # Displays the first 5 rows of the dataset.
    #   print (df.info())           # Shows summary information (column names, data types, non-null counts).
    #   print (df.isnull().sum())   # Counts and displays the number of missing (null) values in each column.

