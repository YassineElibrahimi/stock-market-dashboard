import streamlit as st
import pandas as pd
import plotly.express as px


# PS: the df.index is for the DATE in the CSV file.




# ========================= CLEAR DATA/ BUILD VISUALIZATIONS/ CREATE DASHBORD =========================

def main():
    filename = 'ticker_data.csv'

# import st
    st.set_page_config(layout="wide")
    st.title("📈 S&P 500, Gold, Silver, Dollar, Euro & MAD Dashboard")

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
    df_filtered = df.loc[mask]


# import px
    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 =st.tabs(["S&P 500", "🥇 Gold", "🥈 Silver", "US Dollar", "Euro", "Moroccan Dirham", "All"])

    with tab1:
        fig = px.line(
            df_filtered,
            x=df_filtered.index,            # show only date in CSV file
            y='Close_^GSPC',                # show only 'Close_^GSPC' column
            title='S&P 500 - closing price',
            labels={'value': "Price (USD)", 'Date': "year"}
        )
        # show()
        st.plotly_chart(fig, use_container_width=True)

    with tab2: # Gold may have NaNs, Plotly will skip them
        fig = px.line(
            df_filtered,
            x=df_filtered.index,
            y='Close_GC=F',
            title='GOLD - closing prices',
            labels={'value':"Price (USD)",'Date': "year"}
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        fig = px.line(
            df_filtered,
            x=df_filtered.index,
            y='Close_SI=F',
            title='SILVER - closing price',
            labels={'value':"Price (USD)", 'Date': "year"}
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab4:
        fig = px.line(
            df_filtered,
            x=df_filtered.index,
            y='Close_DX-Y.NYB',
            title='US Dollars - closing price',
            labels={'value': "(USD)", 'Date': "year"}
        )
        # show()
        st.plotly_chart(fig, use_container_width=True)

    with tab5:
        fig = px.line(
            df_filtered,
            x=df_filtered.index,
            y='Close_^XDE',
            title='Euros - closing price',
            labels={'value': "(EURO)", 'Date': "year"}
        )
        # show()
        st.plotly_chart(fig, use_container_width=True)

    with tab6:
        fig = px.line(
            df_filtered,
            x=df_filtered.index,
            y='Close_MAD=X',
            title='Morrocan Dirham - closing price',
            labels={'value': "(MAD)", 'Date': "year"}
        )
        # show()
        st.plotly_chart(fig, use_container_width=True)

    with tab7: 
        fig = px.line(
            df_filtered,
            x=df_filtered.index,
            y=['Close_^GSPC', 'Close_GC=F', 'Close_SI=F', 'Close_DX-Y.NYB', 'Close_^XDE', 'Close_MAD=X'],
            title='All  available "Closing" data',
            labels={'value':"Price (USD)",'Date':"year"}
        )
        st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()