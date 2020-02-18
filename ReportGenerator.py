from functools import reduce

from CryptoDataModel import CryptoDataModel
import datetime
import matplotlib.pyplot as plt


class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def average_bitcoin_price(self):
        average = []
        price = int(reduce(self.add_two_values, self.data) / len(self.data))
        print(price)

    # making sure we add floats together
    @staticmethod
    def add_two_values(a, b):
        if isinstance(a, CryptoDataModel):
            a = a.close

        if isinstance(b, CryptoDataModel):
            b = b.close

        return a + b

    # Todo: get list of weekly btc prices
    def get_all_prices(self):
        bitcoin_prices = []
        dates = []
        for index, item in enumerate(self.data):
            bitcoin_prices.append(int(item.close))

        for index, item in enumerate(self.data):
            timestamp = (int(item.time))
            dates.append(datetime.datetime.fromtimestamp(timestamp))

        dates = [(date.strftime("%a") + ' ' + str(date.day)) for date in dates]

        return bitcoin_prices, dates

    # TODO: think about different type of plots that we can add to pdf
    def plot_btc_prices(self):
        bitcoin_prices, dates = self.get_all_prices()
        plt.plot(dates, bitcoin_prices, 'go--', color='brown', linewidth=1, markersize=12)
        plt.ylabel('Price of a single bitcoin in dollars')
        plt.xlabel('Days of the week')
        plt.show()

    def get_low_high_prices(self):
        open_price = []
        close_price = []
        dates = []
        for index, item in enumerate(self.data):
            open_price.append(int(item.open))
            close_price.append(int(item.close))

        for index, item in enumerate(self.data):
            timestamp = (int(item.time))
            dates.append(datetime.datetime.fromtimestamp(timestamp))

        dates = [(date.strftime("%a") + ' ' + str(date.day)) for date in dates]

        return open_price, close_price, dates

    def plot_open_low_prices(self):
        open_prices, close_prices, dates = self.get_low_high_prices()
        fig, axs = plt.subplots(2, constrained_layout=True)
        axs[0].plot(dates, open_prices)
        axs[0].set_title('Open Prices')
        axs[1].plot(dates, close_prices)
        axs[1].set_title('Close Prices')
        # plt.ylabel('Price of a single bitcoin in dollars')
        # plt.xlabel('Days of the week')
        plt.show()
