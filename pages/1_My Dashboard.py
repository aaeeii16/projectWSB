import streamlit as st
import plotly.graph_objects as go
from getData import getStockData

st.write("# Investment Dashboard")


with st.form("my_form"):
    st.write("## Interactive form")
    stockTicker = st.text_input("What stock do you want to check?\n"
                                "You can choose for example: AAPL for Apple, MSFT for Microsoft or PKO.WA for PKO BP: ")
    stockTicker = stockTicker.upper()

    st.write(f"You picked this stock: {stockTicker}")
    inputPeriod = st.text_input("What is the timespan of the historical data you want to check?\n"
                                "You can choose :'1y', '2y', '5y', '10y', 'ytd', ""'max': ")
    st.form_submit_button('Submit')

    df = getStockData(stockTicker, inputPeriod)
    st.dataframe(df)
    csv_file = df.to_csv('out.csv')

    fig = go.Figure()
    st.write(stockTicker)
    st.write(inputPeriod)
    fig.add_trace(go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close']))
    st.plotly_chart(fig)
