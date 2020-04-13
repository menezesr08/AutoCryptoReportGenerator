import pandas as pd

import Helper
from itertools import repeat
from Plots.BarPlot import BarPlot
from matplotlib import pyplot as plt, dates, ticker
import numpy as np

from Plots.DoubleLinePlot import DoubleLinePlot
from Plots.LinePlot import LinePlot


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
            close_prices = data['close']
            close_prices.index = data['time'].apply(Helper.convert_to_date)

            df_max_prices = pd.DataFrame(
                data.groupby(data['time'].apply(Helper.convert_to_date).dt.week).close.idxmax())
            df_max_prices['price_max'] = data.groupby(
                data['time'].apply(Helper.convert_to_date).dt.week).close.max()

            df_min_prices = pd.DataFrame(
                data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.idxmin())
            df_min_prices['price_min'] = data.groupby(
                data['time'].apply(Helper.convert_to_date).dt.month).close.min()

            ax.plot(close_prices.index, close_prices)
            ax.scatter(df_max_prices['close'], df_max_prices['price_max'], color='blue')
            ax.scatter(df_min_prices['close'], df_min_prices['price_min'], color='red')

            plt.show()

    @staticmethod
    def calc_pct_change(list_of_values):
        first_value = repeat(list_of_values[0], len(list_of_values))
        return [100.0 * a1 / a2 - 100 for a1, a2 in zip(list_of_values[1:], first_value)]
