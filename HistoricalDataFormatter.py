import Helper
from Plots.BarPlot import BarPlot
import matplotlib.pyplot as plt


class HistoricalDataFormatter:
    def __init__(self, data):
        self.data = data

    def create_plots(self):
        self.plot_open_close_prices()

    # figure out how to plot open and close prices
    def plot_open_close_prices(self):
        for crypto_data in self.data:
            open_prices = crypto_data.open
            close_prices = crypto_data.close
            dates = [Helper.format_timestamp(time) for time in crypto_data.time]
            plt.plot(dates, open_prices)
            plt.plot(dates, close_prices)
            plt.show()
            # Todo: so we finally plotted the open and close prices! But the plot looks too basic. Spice it up!'/




