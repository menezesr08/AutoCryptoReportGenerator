import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams


class BarPlot:
    def __init__(self, dates, first_data_set, second_data_set):
        self.first_data_set = first_data_set
        self.second_data_set = second_data_set
        self.dates = dates
        self.width = 0.35

    def plot_open_low_prices(self):
        rcParams['figure.figsize'] = 10, 5
        plt.style.use('fivethirtyeight')
        x_indexes = np.arange(len(self.dates))
        plt.bar(x_indexes - (self.width / 2), self.first_data_set, width=self.width, label='Open prices')
        plt.bar(x_indexes + (self.width / 2), self.second_data_set, width=self.width, color='Red',
                label='Close Prices')
        plt.legend()
        plt.ylabel('Open price vs Close price')
        plt.xlabel('Days')
        plt.subplots_adjust(bottom=.15, left=.10)
        plt.xticks(ticks=x_indexes, labels=self.dates)
        plt.show()

    def plot_high_low_prices(self):
        rcParams['figure.figsize'] = 10, 5
        plt.style.use('fivethirtyeight')
        x_indexes = np.arange(len(self.dates))
        plt.bar(x_indexes - (self.width / 2), self.first_data_set, width=self.width, label='Low prices')
        plt.bar(x_indexes + (self.width / 2), self.second_data_set, width=self.width, color='Red',
                label='High Prices')
        plt.legend()
        plt.ylabel('Low price vs High price')
        plt.xlabel('Days')
        plt.subplots_adjust(bottom=.15, left=.10)
        plt.xticks(ticks=x_indexes, labels=self.dates)
        plt.show()

    def plot_volumefrom_volumeto_prices(self):
        rcParams['figure.figsize'] = 10, 5
        plt.style.use('fivethirtyeight')
        x_indexes = np.arange(len(self.dates))
        plt.bar(x_indexes - (self.width / 2), self.first_data_set, width=self.width, label='Starting Volume')
        plt.bar(x_indexes + (self.width / 2), self.second_data_set, width=self.width, color='Red',
                label='Ending Volume')
        plt.legend()
        plt.ylabel('Starting volume vs ending volume')
        plt.xlabel('Days')
        plt.subplots_adjust(bottom=.15, left=.10)
        plt.xticks(ticks=x_indexes, labels=self.dates)
        plt.show()

