from Plots.LinePlot import LinePlot
import matplotlib.pyplot as plt
import numpy as np


class DoubleLinePlot:
    width = 1
    marker_size = 8

    # def __init__(self, dates, first_data_set, second_data_set):
    #     super().__init__(dates, first_data_set)
    #     self.second_data_set = second_data_set
    #     self.get_min_max()

    @classmethod
    def plot_open_close_prices(cls, dates, open_prices, close_prices, label):
        plt.plot(dates, open_prices, color='blue', linewidth=cls.width,
                 label='Open Price')
        plt.plot(dates, close_prices, color='red', linewidth=cls.width,
                 label='Close Price')
        plt.title(label)
        plt.xlabel('Days of the week')
        plt.ylabel('Price of a single bitcoin')
        plt.legend()
        plt.show()

        # Todo: think about the best data to plot. Might be worth plotting different currencies rather than one Might
        #  be worth showing data from 30 days so you have more data on the screen. You can make date x axis sideways
        #  to save space like in these examples:
        #  https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/

    # # finish this method. Look at different subplots
    # def plot_volumefrom_volumeto_prices(self):
    #     fig, (ax1, ax2) = plt.subplots(2)
    #     fig.suptitle('Vertically stacked subplots')
    #     ax1.plot(self.dates, self.data, 'go--', color='brown', linewidth=self.line_width,
    #              markersize=self.marker_size)
    #     ax1.set_xlabel('Days of the week')
    #     ax1.set_ylabel('Volume at the start of the day')
    #     ax2.plot(self.dates, self.second_data_set, 'go--', color='brown', linewidth=self.line_width,
    #              markersize=self.marker_size)
    #     ax2.set_xlabel('Days of the week')
    #     ax2.set_ylabel('Volume at the end of the day')
    #     formatted_y = [self.human_format(num) for num in self.get_min_max()]
    #     ax2.set_yticks(self.get_min_max())
    #     ax2.set_yticklabels(formatted_y)
    #     plt.show()

    def get_min_max(self):
        sorted_volumes = sorted(self.second_data_set)
        min_volume, max_volume = sorted_volumes[0], sorted_volumes[-1]
        values = np.linspace(min_volume, max_volume, num=len(self.second_data_set))
        return values

    # converts huge numbers into a readable format
    @staticmethod
    def human_format(num):
        num = float('{:.2g}'.format(num))
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
