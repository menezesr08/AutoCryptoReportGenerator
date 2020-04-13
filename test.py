import pickle

import pandas as pd

import matplotlib.dates as mdates

from datetime import datetime

from matplotlib.ticker import FuncFormatter

import Helper
from CryptoReport import CryptoReport
from Plots import LinePlot

import matplotlib.pyplot as plt

report = CryptoReport(["BTC"])
api = pickle.load(open("save.p", "rb"))


# report.get_crypto_historical_data()


# for crypto_data in data:
#     fig, ax = plt.subplots(constrained_layout=True)
#     data = crypto_data['data']
#
#     close_prices = data['close']
#     close_prices.index = data['time'].apply(Helper.convert_to_date)
#     close_prices.groupby(by=[close_prices.index.month, close_prices.index.year])
#
#     df_max = pd.DataFrame(data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.idxmax())
#     df_max['price_max'] = data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.max()
#
#     ax.plot(close_prices.index, close_prices)
#     ax.scatter(df_max['close'], df_max['price_max'], color='blue')
#
#     df_min = pd.DataFrame(data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.idxmin())
#     df_min['price_min'] = data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.min()
#
#     ax.plot(close_prices.index, close_prices)
#     ax.scatter(df_min['close'], df_min['price_min'], color = 'red')
#
#     # locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
#     # formatter = mdates.ConciseDateFormatter(locator)
#     # ax.xaxis.set_major_locator(locator)
#     # ax.xaxis.set_major_formatter(formatter)
#     ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
#
#     plt.show()

def plot_close_prices():
    for crypto_data in api:
        fig, ax = plt.subplots(constrained_layout=True)
        data = crypto_data['data']
        close_prices = data['close']
        close_prices.index = data['time'].apply(Helper.convert_to_date)

        df_max = pd.DataFrame(data.groupby(data['time'].apply(Helper.convert_to_date).dt.week).close.idxmax())
        df_max['price_max'] = data.groupby(data['time'].apply(Helper.convert_to_date).dt.week).close.max()

        df_min = pd.DataFrame(data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.idxmin())
        df_min['price_min'] = data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.min()

        ax.plot(close_prices.index, close_prices)
        ax.scatter(df_max['close'], df_max['price_max'], color='blue')
        ax.scatter(df_min['close'], df_min['price_min'], color='red')

        plt.show()


weekly_plot_data()
