import streamlit as st
import yfinance as yf
import datetime

st.header("This is stock market data")

#Textbox
ticker_symbol = st.text_input('Enter Stock Symbol', 'APPL', key='placeholder')

ticker_data = yf.Ticker(ticker_symbol)



#Date inpput
col1, col2 = st.columns(2)

with col1:
   st.header("Input Starting Date")
   start_date = st.date_input("Input Starting date", datetime.date(2019, 7, 6))

with col2:
   st.header("Input Ending date")
   end_date = st.date_input("Input Starting date", datetime.date(2022, 12, 31))

ticker_df = ticker_data.history(period='1d',start=f'{start_date}',end=f'{end_date}')

dicter = {'AAPL':'APPLE','GOOG':'GOOGLE'}

st.write(f"""
        
        {dicter[ticker_symbol]} stock price analysis:

        """)

st.dataframe(ticker_df)

#Linechart
col1, col2 = st.columns(2)

with col1:
   st.header("Volume Analysis")
   st.line_chart(ticker_df['Volume'])

with col2:
   st.header("Closing Analysis")
   st.line_chart(ticker_df['Close'])



