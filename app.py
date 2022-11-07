import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import requests
import io

# url = "https://alpha-vantage.p.rapidapi.com/query"
#
# querystring = {"interval": "5min", "function": "TIME_SERIES_INTRADAY", "symbol": "MSFT", "datatype": "csv",
#                "output_size": "compact"}
#
# headers = {
#     "X-RapidAPI-Key": "5d8f88f3dfmsh8f8745701f427c2p166500jsnb0867550681d",
#     "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
# # save the data as csv file
# with open('data.csv', 'w') as f:
#     writer = csv.writer(f)
#     for row in response.iter_lines():
#         writer.writerow(row.decode('utf-8').split(','))
# # read the csv file

"st.session_state object:", st.session_state

st.title("Alpha Vantage API")
st.markdown("This app retrieves stock data for the last 7 days!")

# create main streamlit section
st.header('Main Section')
# st selectbox for stock ticker
stock_ticker = st.selectbox('Select Stock Ticker', ('MSFT', 'AAPL', 'GOOG', 'AMZN', 'FB', 'TSLA', 'NFLX', 'NVDA', 'PYPL', 'ADBE'))
# st selectbox for stock interval
stock_interval = st.selectbox('Select Stock Interval', ('1min', '5min', '15min', '30min', '60min'))
# st selectbox for stock function
stock_function = st.selectbox('Select Stock Function', ('TIME_SERIES_INTRADAY', 'TIME_SERIES_DAILY', 'TIME_SERIES_WEEKLY', 'TIME_SERIES_MONTHLY'))
# st selectbox for stock datatype
stock_datatype = st.selectbox('Select Stock Datatype', ('csv', 'json'))
# st selectbox for stock output size
stock_output_size = st.selectbox('Select Stock Output Size', ('compact', 'full'))

# create url for API request
# on click of a button fetch the data
# clear the session state
# st.session_state.clear()
fetch = st.button('Fetch Data')
# check if session state fetch is empty
if 'fetch' not in st.session_state:
    st.session_state['fetch'] = False
if 'fetch' in st.session_state == True:
    st.write('Fetching data...')
else :
    st.session_state['fetch'] = True
    url = "https://alpha-vantage.p.rapidapi.com/query"
    querystring = {"interval": stock_interval, "function": stock_function, "symbol": stock_ticker, "datatype": stock_datatype,"output_size": stock_output_size}
    headers = {"X-RapidAPI-Key": "5d8f88f3dfmsh8f8745701f427c2p166500jsnb0867550681d","X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"}
    if 'response' not in st.session_state:
        st.session_state = {'response': requests.request("GET", url, headers=headers, params=querystring)}
        st.session_state ['stock_datatype'] = stock_datatype
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code == 200:
        st.write('Data fetched successfully')
        st.session_state['response'] = response
        st.session_state ['stock_datatype'] = stock_datatype
        # save the data as csv file
        with open('data1.csv', 'w') as f:
            writer = csv.writer(f)
            for row in response.iter_lines():
                writer.writerow(row.decode('utf-8').split(','))
    # display the data fetched from the API as either csv or json
    st.header('Fetched Data from API')
    # check if the data is in csv format and make it not closeable
    # print st.session_state
    st.write(st.session_state)


    # if stock_datatype == 'csv':
    if st.session_state['stock_datatype'] == 'csv':
        # slider to ask and show how many results to show
        # calculate the number of rows of response results
        df = pd.read_csv(io.StringIO(st.session_state['response'].text))
        lendf = len(df)
        st.write('Row count is:', len(df))

        number = st.slider('Number of Results shown', min_value=1, max_value=lendf, value=10, step=10, key="slider")
        # get slider value
        # st.session_state['slider_value'] = st.session_state['slider_value']
        # print slider value
        st.write("Slider Value:", number)
        if st.checkbox('Show all data'):
            raw_data1 = pd.read_csv(io.StringIO(response.text))
            st.write(raw_data1)
        else:
            # show interactive table of data
            # st.write(response.text[:500])
            # show 10 rows of data from response
            rawdata = pd.read_csv(io.StringIO(response.text))
            st.write(rawdata.head(number))

        # ask user how to display the data as interactive table, chart, line graph, area chart, bar chart, pie chart
        # st selectbox for stock display
        stock_display = st.selectbox('Select Stock Display format', ('Interactive Table', 'Chart', 'Line Graph', 'Area Chart', 'Bar Chart', 'Map'))
        # if stock_display == 'Interactive Table':
        if stock_display == 'Interactive Table':
            # read the csv file
            df = pd.read_csv('data.csv')
            # display the data as interactive table
            st.write(df)
        # elif stock_display == 'Chart':
        elif stock_display == 'Chart':
            # read the csv file data and put into array
            dfa = pd.read_csv('data1.csv')
            #select the columns to display
            # st.write(dfa[['timestamp', 'open', 'high', 'low', 'close']])
            dfc = dfa[['open', 'high', 'low', 'close']]
            st.line_chart(dfc)

        # elif stock_display == 'Line Graph':
        elif stock_display == 'Line Graph':
            # read the csv file
            dfa = pd.read_csv('data1.csv')
            # select the columns to display
            # st.write(dfa[['timestamp', 'open', 'high', 'low', 'close']])
            dfc = dfa[['open', 'high', 'low', 'close']]
            st.line_chart(dfc)
        # elif stock_display == 'Area Chart':
        elif stock_display == 'Area Chart':
            dfa = pd.read_csv('data1.csv')
            # st.write(dfa[['timestamp', 'open', 'high', 'low', 'close']])
            dfc = dfa[['open', 'high', 'low', 'close']]
            st.area_chart(dfc)
        # elif stock_display == 'Bar Chart':
        elif stock_display == 'Bar Chart':
            dfa = pd.read_csv('data1.csv')
            # st.write(dfa[['timestamp', 'open', 'high', 'low', 'close']])
            dfc = dfa[['open', 'high', 'low', 'close']]
            st.bar_chart(dfc)
        # elif stock_display == 'Pie Chart':
        elif stock_display == 'Map':
            # dfa = pd.read_csv('data1.csv')
            # # st.write(dfa[['timestamp', 'open', 'high', 'low', 'close']])
            # dfc = dfa[['open', 'high', 'low', 'close']]
            # st.map(dfc)
            df = pd.DataFrame(
                np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                columns=['lat', 'lon'])

            st.map(df)
    else:
        # limit the data to 500 characters
        st.write(response.text[:500])
        if (st.checkbox('Show full data')):
            stock_datatype = 'json'
            st.write(response.text)

        #  drop down to ask user to plot the data as
        # either line or bar chart




# # create a section for the dataframe statistics
# st.header('Statistics of Dataframe')
# # st write the dataframe statistics
# df = pd.read_csv('data.csv')
# st.write(df.describe())
#
# # on click of button, get the stock data corresponding to the selected options
# if st.button('Get Stock Data'):
#     # st write the dataframe header
#     st.header('Header of Dataframe')
#     st.write(df.head())
#
#     # st write the dataframe plot
#     st.header('Plot of Data')
#     fig, ax = plt.subplots(1, 1)
#     ax.scatter(x=df['timestamp'], y=df['close'])
#     ax.set_xlabel('timestamp')
#     ax.set_ylabel('close')
#     st.pyplot(fig)
#
# # choose a chart, line, bar, scatter, etc then plot the data
# # st write the dataframe plot
# st.header('Plot of Data')
# fig, ax = plt.subplots(1, 1)
# ax.scatter(x=df['timestamp'], y=df['close'])
# ax.set_xlabel('timestamp')
# ax.set_ylabel('close')
# st.pyplot(fig)
#
# # create a section for the dataframe statistics
# st.header('Statistics of Dataframe')
# # st write the dataframe statistics
# df = pd.read_csv('data.csv')
# st.write(df.describe())

