import quandl
import pandas_datareader.data as web
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(1970,1,1)
end = datetime.datetime(2018,9,18)



###############################################
#              DATA GETS                      #
###############################################
# This method pulls the requested data frame from storage to the application
def get_data_frame(ticker, file_type):
    df = pd.read_csv('/Users/mac/Desktop/Finance/Historical_Stock_Data/{}'.format(ticker) + '_dataframe' + str(file_type))




###############################################
#                YAHOO FINANCE                #
#                   stocks                    #
#                most reliable                #
#                30 years back                #
#              total float points             #
###############################################

def data_peek(ticker):
    df = web.DataReader(ticker, 'yahoo', start, end)
    print df.head()
    print df.tail()

data_peek('OVTZ')

def yahoo_grab_to_csv(ticker):
    yahoo_df = web.DataReader(ticker, 'yahoo', start, end)
    yahoo_df.to_csv('/Users/mac/Desktop/Finance/Historical_Stock_Data/Yahoo/' + str(ticker) + '_daily.csv')
    print yahoo_df.head()

def yahoo_grab_to_excel(ticker):
    yahoo_df = web.DataReader(ticker, 'yahoo', start, end)
    yahoo_df.to_excel('/Users/mac/Desktop/Finance/Historical_Stock_Data/Yahoo/' + str(ticker) + '_yahoo_dataframe.xlsx')
    print yahoo_df.head()


# yahoo_grab_to_csv('BIOS')



###############################################
#                IEX FINANCE                  #
#                  stocks                     #
#                  5Years                     #
#                 Reliable                    #
#            rounds 0.001 place               #
###############################################
def iex_grab_to_csv(ticker):
    start = datetime.datetime(2013,9,18)
    end = datetime.datetime(2018,9,18)
    iex_df = web.DataReader(str(ticker), 'iex', start, end)
    iex_df.to_csv('/Users/mac/Desktop/Finance/Historical_Stock_Data/' + str(ticker) + '_iex_dataframe.csv')

def iex_grab_to_excel(ticker):
    start = datetime.datetime(2013,9,18)
    end = datetime.datetime(2018,9,18)
    iex_df = web.DataReader(str(ticker), 'iex', start, end)
    iex_df.to_excel('/Users/mac/Desktop/Finance/Historical_Stock_Data/' + str(ticker) + '_iex_dataframe.xlsx')




###############################################
#                GOOGLE FINANCE               #
#                   stocks                    #
#                  breaking                   #
#                 data issues                 #
###############################################
# def google_grab_to_csv(ticker):
    # google_df = web.DataReader(ticker, 'google', start, end)
    # google_df.to_csv('/Users/mac/Desktop/Finance/Historical_Stock_Data/' + str(ticker) + '_google_dataframe.csv')

# def google_grab_to_excel(ticker):
#     google_df = web.DataReader(ticker, 'google', start, end)
#     google_df.to_excel('/Users/mac/Desktop/Finance/Historical_Stock_Data/' + str(ticker) + '_google_dataframe.xlsx')








# yahoo_grab_to_csv('FB')
# iex_grab_to_csv('FB')



###############################################
#                STOOQ FINANCE                #
#                   stocks                    #
#                   5 Years                   #
#              sketchy af source              #
###############################################
# def stooq_grab_to_csv(ticker):
#     start = datetime.datetime(2013,1,1)
#     end = datetime.datetime(2018,9,18)
#
#     df = web.stooq.StooqDailyReader('FB', start, end)
#     print df.head()
#     # stooq_df.to_csv('/Users/mac/Desktop/Finance/Historical_Stock_Data/' + str(ticker) + '_dataframe.csv')
#
# def stooq_grab_to_excel(ticker):
#     start = datetime.datetime(2013,9,18)
#     end = datetime.datetime(2018,9,18)
#     stooq_df = web.DataReader('^' + str(ticker), 'stooq')
#     stooq_df.to_csv('/Users/mac/Desktop/Finance/Historical_Stock_Data/' + str(ticker) + '_dataframe.xlsx')



###############################################
#                QUANDL FINANCE               #
#                   futures                   #
#                   13 Years                  #
#                 - BAD DATA -                #
###############################################
# def quandl_grab_to_csv(quandle_code):
#     df = quandl.get(quandle_code, returns='numpy', parse_dates=True)
#     compiled_df = pd.DataFrame(df)
#     compiled_df.to_csv('/Users/mac/Desktop/Finance/Historical_Stock_Data/{}'.format(quandle_code.split('/')) + '_dataframe.csv')
#
# # drops dates attribute data is very questionable
# def quandl_grab_to_excel(quandle_code):
#     df = quandl.get(quandle_code, returns='numpy')
#     compiled_df = pd.DataFrame(df)
#     compiled_df.to_excel('/Users/mac/Desktop/Finance/Historical_Stock_Data/{}'.format(quandle_code.split('/')) + '_dataframe.xlsx')




###############################################
#             PING DATA SOURCES               #
#                1. Yahoo                     #
#                2. Google                    #
#                3. IEX                       #
#                4. Stooq   -  sketchy source #
#                5. Quandl  -  bad data       #
###############################################
#  Pinging Data sources for
#  1.) data_points
#  2.) time_frames
#  The average so far is 6 years back available for free

# def ping(*quandl_code, **ticker):

    # yahoo_df = web.DataReader(str(ticker), 'yahoo', start, end)
    # print 'Yahoo Finance .HEAD() results:'
    # print yahoo_df.head()
    # print 'Yahoo Finance .TAIL() results:'
    # print yahoo_df.tail()
    #
    # google_df = web.DataReader(str(ticker), 'google', start, end)
    # print 'Google Finance .HEAD() results:'
    # print google_df.head()
    # print 'Google Finance .TAIL() results:'
    # print google_df.tail()
    #
    # iex_df = web.DataReader(str(ticker), 'iex', start, end)
    # print 'IEX Finance .HEAD() results:'
    # print iex_df.head()
    # print 'IEX Finance .TAIL() results:'
    # print iex_df.tail()

    # stooq_df = web.DataReader('^' + str(ticker), 'stooq')
    # print 'Stooq Finance .HEAD() results:'
    # print stooq_df.head()
    # print 'Stooq Finance .TAIL() results:'
    # print stooq_df.tail()

    # quandl_df = quandl.get(str(quandl_code))
    # print 'Quandl Finance DF.HEAD() results:'
    # print dquandl_dff.head()
    # print 'Quandl Finance DF.TAIL() results:'
    # print dquandl_dff.tail()
