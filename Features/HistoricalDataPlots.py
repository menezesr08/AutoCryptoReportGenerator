import pandas as pd

import Helper
from matplotlib import pyplot as plt

from Features.Plots.MonthlyPlot import MonthlyPlot
from Features.Plots.WeeklyPlot import WeeklyPlot
from Features.Plots.YearlyPlot import YearlyPlot


class HistoricalDataPlots:
    def __init__(self, data):
        self.data = data

    def create_plot(self):
        self.plot_close_prices()

    # figure out how to plot open and close prices
    def plot_close_prices(self):
        # plot = WeeklyPlot(self.data, self.calculate_simple_moving_average, self.calculate_exponential_moving_average)
        # plot.create_plot()
        plot = MonthlyPlot(self.data, self.calculate_simple_moving_average, self.calculate_exponential_moving_average)
        plot.create_plot()
        # plot = YearlyPlot(self.data, self.calculate_simple_moving_average, self.calculate_exponential_moving_average)
        # plot.create_plot()

        # fig, ax = plt.subplots(constrained_layout=True)
        # fig.set_size_inches(7, 5)
        # # get relevant data from outer dataframe
        # data = self.data['data']
        # data['time'] = data['time'].apply(Helper.convert_to_date)
        # time_period = self.data['time_period']
        # window_size = self.data['window']
        # close_prices = data['close']
        # close_prices_dates = data['time']
        #
        # if time_period.value != "days":
        #     df_max_prices, df_min_prices = self.get_max_and_min__prices(data, time_period)
        #     sim_moving_average = self.calculate_simple_moving_average(close_prices, window_size.value)
        #     exp_moving_average = self.calculate_exponential_moving_average(close_prices, window_size.value)
        #     # ax.scatter(df_max_prices['close'], df_max_prices['price_max'], marker="^", color='blue')
        #     # ax.scatter(df_min_prices['close'], df_min_prices['price_min'], marker="v", color='red')
        #     ax.plot(exp_moving_average.index, exp_moving_average,
        #             linestyle="--", label="EX")
        #     ax.plot(sim_moving_average.index, sim_moving_average,
        #             linestyle=":")
        #
        # ax.plot(close_prices.index, close_prices, linestyle="-")

        # plt.xticks(rotation=45)
        # plt.savefig('images/plot - {0}'.format(Helper.todays_date()))

    # @staticmethod
    # def get_max_and_min__prices(data, time_period):
    #
    #     df_max_prices = None
    #     df_min_prices = None
    #
    #     if time_period.value == "week":
    #         df_max_prices = data.groupby(
    #             data['time'].dt.week).close.max()
    #
    #         df_min_prices = data.groupby(
    #             data['time'].dt.week).close.min()
    #
    #     elif time_period.value == "month":
    #         df_max_prices = pd.DataFrame(
    #             data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.idxmax())
    #         df_max_prices['price_max'] = data.groupby(
    #             data['time'].apply(Helper.convert_to_date).dt.month).close.max()
    #
    #         df_min_prices = pd.DataFrame(
    #             data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.idxmin())
    #         df_min_prices['price_min'] = data.groupby(
    #             data['time'].apply(Helper.convert_to_date).dt.month).close.min()
    #
    #     elif time_period.value == "year":
    #         df_max_prices = pd.DataFrame(
    #             data.groupby(data['time'].apply(Helper.convert_to_date).dt.year).close.idxmax())
    #         df_max_prices['price_max'] = data.groupby(
    #             data['time'].apply(Helper.convert_to_date).dt.year).close.max()
    #
    #         df_min_prices = pd.DataFrame(
    #             data.groupby(data['time'].apply(Helper.convert_to_date).dt.year).close.idxmin())
    #         df_min_prices['price_min'] = data.groupby(
    #             data['time'].apply(Helper.convert_to_date).dt.year).close.min()
    #
    #     return df_max_prices, df_min_prices
    @staticmethod
    def calculate_exponential_moving_average(data, window_size):
        short_rolling = data.ewm(span=window_size, adjust=False).mean()
        return short_rolling

    @staticmethod
    def calculate_simple_moving_average(data, window_size):
        short_rolling = data.rolling(window=window_size, min_periods=1).mean()
        return short_rolling
