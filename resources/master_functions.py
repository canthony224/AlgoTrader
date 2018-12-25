import pandas as pd



# Example Account dict
# account dict ={"NAME":"Main Account,
#                "ID":123456789,
#                "TOKEN":999977744499,
#                "MISC":"extra_data_possibly_needed"}


def get_ticker_bars(ticker, bar_granularity, broker, account_dict, bar_amount=1):
    """
    :param ticker: [string] the currency to get bars from (EUR_USD, GBP_NZD... etc)
    :param bar_granularity: [string] the density of the bars. (5M,10M,15M,30M,1H,4H,8H,12H,1D,1W,1M)
    :param bar_amount: [int] number of bars to get. The default is 1 bar.
    :param broker: [string] specific broker to get data from.
    :param account_dict: dictionary holding data about the specific account.
    :return: Pandas data-frame object with Open,High,Low,Close,Volume data
    """

    # Check What Broker is requested
    if broker == "oanda":



