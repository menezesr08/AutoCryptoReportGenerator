import pandas as pd

import Helper
from itertools import repeat
from Plots.BarPlot import BarPlot
from matplotlib import pyplot as plt, dates, ticker
import numpy as np

from Plots.DoubleLinePlot import DoubleLinePlot
from Plots.LinePlot import LinePlot
from enums.TimePeriods import TimePeriods


class HistoricalDataPlots:
    def __init__(self, data):
        self.data = data

    def create_plots(self):
        self.plot_close_prices()

    # figure out how to plot open and close prices
    def plot_close_prices(self):
        for crypto_data in self.data:
            fig, ax = plt.subplots(constrained_layout=True)
            # get relevant data from outer dataframe
            data = crypto_data['data']
            time_period = crypto_data['time_period']
            close_prices = data['close']
            close_prices.index = data['time'].apply(Helper.convert_to_date)

            df_max_prices = self.get_max_prices(data, time_period)
            df_min_prices = self.get_min_prices(data, time_period)

            ax.plot(close_prices.index, close_prices)
            ax.scatter(df_max_prices['close'], df_max_prices['price_max'], color='blue')
            ax.scatter(df_min_prices['close'], df_min_prices['price_min'], color='red')

            plt.show()

    @staticmethod
    def get_max_prices(data, time_period):

        if time_period in TimePeriods and time_period.value is "week":
            df_max_prices = pd.DataFrame(
                data.groupby(data['time'].apply(Helper.convert_to_date).dt.week).close.idxmax())
            df_max_prices['price_max'] = data.groupby(
                data['time'].apply(Helper.convert_to_date).dt.week).close.max()

            return df_max_prices
        elif time_period in TimePeriods and time_period.value is "month":
            df_max_prices = pd.DataFrame(
                data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.idxmax())
            df_max_prices['price_max'] = data.groupby(
                data['time'].apply(Helper.convert_to_date).dt.month).close.max()

            return df_max_prices
        elif time_period in TimePeriods and time_period.value is "year":
            df_max_prices = pd.DataFrame(
                data.groupby(data['time'].apply(Helper.convert_to_date).dt.year).close.idxmax())
            df_max_prices['price_max'] = data.groupby(
                data['time'].apply(Helper.convert_to_date).dt.year).close.max()

            return df_max_prices

    @staticmethod
    def get_min_prices(data, time_period):

        if time_period in TimePeriods and time_period.value is "week":
            df_min_prices = pd.DataFrame(
                data.groupby(data['time'].apply(Helper.convert_to_date).dt.week).close.idxmin())
            df_min_prices['price_min'] = data.groupby(
                data['time'].apply(Helper.convert_to_date).dt.week).close.min()

            return df_min_prices
        elif time_period in TimePeriods and time_period.value is "month":
            df_min_prices = pd.DataFrame(
                data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.idxmin())
            df_min_prices['price_min'] = data.groupby(
                data['time'].apply(Helper.convert_to_date).dt.month).close.min()

            return df_min_prices
        elif time_period in TimePeriods and time_period.value is "year":
            df_min_prices = pd.DataFrame(
                data.groupby(data['time'].apply(Helper.convert_to_date).dt.year).close.idxmin())
            df_min_prices['price_min'] = data.groupby(
                data['time'].apply(Helper.convert_to_date).dt.year).close.min()

            return df_min_prices
