from functools import reduce

from CryptoDataModel import CryptoDataModel
import datetime
import matplotlib.pyplot as plt
import Helper


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
        open_prices, close_prices = self.get_specific_bitcoin_data("open", "close")
        # fig, axs = plt.subplots(2, constrained_layout=True)
        # axs[0].plot(dates, open_prices)
        # axs[0].set_title('Open Prices')
        # axs[1].plot(dates, close_prices)
        # axs[1].set_title('Close Prices')
        # # plt.ylabel('Price of a single bitcoin in dollars')
        # # plt.xlabel('Days of the week')
        # plt.show()
        plt.plot(open_prices, close_prices, 'go--', color='brown', linewidth=1, markersize=8)
        plt.ylabel('Price of a single bitcoin in dollars')
        plt.xlabel('Days of the week')
        plt.show()

    def plot_btc_prices(self):
        bitcoin_prices = self.get_all_prices()
        plt.plot(self.dates, bitcoin_prices, 'go--', color='brown', linewidth=1, markersize=8)
        plt.ylabel('Price of a single bitcoin in dollars')
        plt.xlabel('Days of the week')
        plt.show()

    def get_all_dates(self):
        dates = []
        for item in self.data:
            timestamp = (int(item.time))
            dates.append(datetime.datetime.fromtimestamp(timestamp))

        dates = [(date.strftime("%a") + ' ' + str(date.day)) for date in dates]
        return dates

    # Todo: watch corey's matplotlib tutorial to get some ideas on different types of plots you could create
