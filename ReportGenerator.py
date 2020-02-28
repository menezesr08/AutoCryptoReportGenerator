from functools import reduce

from CryptoDataModel import CryptoDataModel
import datetime
import numpy as np
import matplotlib.pyplot as plt
import Helper
from LinePlot import LinePlot


class ReportGenerator:
    def __init__(self, data):
        self.data = data
        self.dates = self.get_all_dates()

    def average_bitcoin_price(self):
        price = int(sum(daily_stats.close for daily_stats in self.data)) / len(self.data)
        average = []
        return price

    def get_all_prices(self):
        bitcoin_prices = []
        for item in self.data:
            bitcoin_prices.append(int(item.close))

        return bitcoin_prices

    # The following selects part of the JSON data as requested.
    # The method takes any two attributes as parameters and returns all the data matching these attributes
    def get_specific_bitcoin_data(self, first_attribute, second_attribute):
        first_attribute_values = []
        second_attribute_values = []
        for item in self.data:
            first_attribute_values.append(int(getattr(item, first_attribute)))
            second_attribute_values.append(int(getattr(item, second_attribute)))

        return first_attribute_values, second_attribute_values

    def plot_open_low_prices(self):
        plt.style.use('fivethirtyeight')
        x_indexes = np.arange(len(self.dates))
        width = 0.35
        open_prices, close_prices = self.get_specific_bitcoin_data("open", "close")
        plt.bar(x_indexes - (width/2), open_prices, width=width,  label="Open Prices")
        plt.bar(x_indexes + (width/2), close_prices, width=width, color='#444444',  label="Close Prices")
        plt.legend()
        plt.xticks(ticks=x_indexes, labels=self.dates)
        plt.xlabel('Days')
        plt.ylabel('Price of a single bitcoin in dollars')
        plt.tight_layout()
        plt.show()

    def plot_btc_prices(self):
        plot = LinePlot(self.get_all_dates(), self.get_all_prices(), color="brown")
        plot.plot_data()

    def get_all_dates(self):
        dates = []
        for item in self.data:
            timestamp = (int(item.time))
            dates.append(Helper.get_date(timestamp))

        dates = [Helper.format_date(date) for date in dates]
        return dates

    # Todo: watch corey's matplotlib tutorial to get some ideas on different types of plots you could create
    # Todo: Hide Api Key
