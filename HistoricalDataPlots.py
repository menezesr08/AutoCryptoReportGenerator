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
        self.plot_open_close_prices()

    # figure out how to plot open and close prices
    def plot_open_close_prices(self):
        for crypto_data in self.data:
            data = crypto_data['data']
            title = crypto_data['title']

            close_prices = data['close']
            close_prices.index = data['time'].apply(Helper.format_timestamp)
            LinePlot.plot_historical_data(title, close_prices)

            # slicing data -- open_prices.loc['Feb 21 2016': 'Oct 28 2016'].plot()
            # close_prices = self.calc_pct_change(crypto_data.close)
            # formatted_dates = [Helper.format_timestamp(time) for time in crypto_data.time]
            # fig, ax = plt.subplots()
            # ax.plot_date(formatted_dates[1:], open_prices, '-')
            # locator = dates.MonthLocator()
            # ax.xaxis.set_major_locator(locator)
            # plt.plot(dates[1:], open_prices, label=crypto_data.title)

            # DoubleLinePlot.plot_open_close_prices(dates, open_prices, close_prices, crypto_data.title)
            # Todo: so we managed to plot lines. However too many lines in a plot looks too populated. Maybe use bar
            #  or some other method. You could use subplots as suggested here:
            #  Check out historail data on crypto compare and figure out what aggregrate is. Maybe you can plot
            #  data from different time periods
            # https://stackoverflow.com/questions/4805048/how-to-get-different-colored-lines-for-different-plots-in-a-single-figure

    @staticmethod
    def calc_pct_change(list_of_values):
        first_value = repeat(list_of_values[0], len(list_of_values))
        return [100.0 * a1 / a2 - 100 for a1, a2 in zip(list_of_values[1:], first_value)]
