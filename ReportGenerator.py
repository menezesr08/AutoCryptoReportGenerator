from functools import reduce

from BarPlot import BarPlot
from CryptoDataModel import CryptoDataModel
import datetime
import numpy as np
import matplotlib.pyplot as plt
import Helper
from DoubleLinePlot import DoubleLinePlot
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

    def plot_open_close_prices(self):
        open_prices, close_prices = self.get_specific_bitcoin_data('open', 'close')
        bar_plot = BarPlot(self.get_all_dates(), open_prices, close_prices)
        bar_plot.plot_open_close_prices()

    def plot_high_low_prices(self):
        low_prices, high_prices = self.get_specific_bitcoin_data('high', 'low')
        bar_plot = BarPlot(self.get_all_dates(), high_prices, low_prices)
        bar_plot.plot_high_low_prices()

    def plot_volumefrom_volumeto_price(self):
        volume_from, volume_to = self.get_specific_bitcoin_data('volumefrom', 'volumeto')
        subplot = DoubleLinePlot(self.get_all_dates(), volume_from, volume_to)
        subplot.plot_volumefrom_volumeto_prices()

    def plot_btc_prices(self):
        line_plot = LinePlot(self.get_all_dates(), self.get_all_prices())
        line_plot.plot_bitcoin_price()

    def get_all_dates(self):
        dates = []
        for item in self.data:
            timestamp = (int(item.time))
            dates.append(Helper.get_date(timestamp))

        dates = [Helper.format_date(date) for date in dates]
        return dates

    @staticmethod
    def human_format(num):
        num = float('{:.3g}'.format(num))
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])

    # Todo: Hide Api Key
