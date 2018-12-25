

def get_ticker_bars(ticker, bar_granularity, bar_amount=1):
    """
    :param ticker: the currency to get bars from
    :param bar_granularity: the density of the bars. (5M,10M,15M,30M,1H,4H,8H,12H,1D,1W,1M)
    :param bar_amount: number of bars to get. The default is 1 bar.
    :return: Pandas data-frame object with Open,High,Low,Close,Volume data
    """