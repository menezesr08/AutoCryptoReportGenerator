import matplotlib.pyplot as plt
import numpy as np
from pylab import rcParams


class BarPlot:
    width = 0.35

    @classmethod
    def plot_open_close_prices(cls, dates, open_prices, close_prices, label):
        rcParams['figure.figsize'] = 10, 5
        plt.style.use('fivethirtyeight')
        x_indexes = np.arange(len(dates))
        plt.bar(x_indexes - (cls.width / 2), open_prices, width=cls.width, label='Open prices')
        plt.bar(x_indexes + (cls.width / 2), close_prices, width=cls.width, color='Red',
                label='Close Prices')
        plt.legend()
        plt.title = label
        plt.ylabel('Open price vs Close price')
        plt.xlabel('Days')
        plt.subplots_adjust(bottom=.15, left=.10)
        plt.xticks(ticks=x_indexes, labels=dates)
        plt.show()
        # plt.savefig(f'images/{label}_plot.png')

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
