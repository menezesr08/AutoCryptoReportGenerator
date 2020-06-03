import itertools

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from dateutil.rrule import MO

import Helper
from enums.PlotLabels import PlotLabels


class WeeklyPlot:

    def __init__(self, crypto_data_dict, simple_moving_average, exponential_moving_average):
        self.crypto_data_dict = crypto_data_dict
        self.sma = simple_moving_average
        self.ema = exponential_moving_average
        self.fig = plt.figure()

        self.ax = self.fig.add_subplot(111)
        self.ax.grid(True)
        # self.ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
        self.ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=MO))
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%a %d %b'))

    def create_plot(self):
        formatted_data = self.format_data(self.crypto_data_dict)
        weekly_min_prices, weekly_max_prices, simple_moving_average, exponential_moving_average = \
            self.calculate_statistics(formatted_data)
        x = formatted_data['time']
        y = formatted_data['close']
        self.ax.plot(x, y)
        self.ax.plot(formatted_data['time'], simple_moving_average, color='blue')
        self.ax.plot(formatted_data['time'], exponential_moving_average, color='red')
        self.ax.scatter(weekly_max_prices['time'], weekly_max_prices['close'], marker="^", color='blue')
        self.ax.scatter(weekly_min_prices['time'], weekly_min_prices['close'], marker="^", color='red')
        self.fig.autofmt_xdate()
        plt.title(PlotLabels.monthly_plot_title.value)
        plt.xlabel(PlotLabels.monthly_plot_x.value)
        plt.ylabel(PlotLabels.y_title.value)
        plt.show()
        # plt.savefig('images/plot - {0}'.format(Helper.todays_date()))

    def calculate_statistics(self, formatted_data):
        weekly_min_prices = self.min_close_per_week(formatted_data[['time', 'close']])
        weekly_max_prices = self.max_close_per_week(formatted_data[['time', 'close']])
        simple_moving_average = self.sma(formatted_data['close'], self.crypto_data_dict['window'].value)
        exponential_moving_average = self.ema(formatted_data['close'], self.crypto_data_dict['window'].value)
        return weekly_min_prices, weekly_max_prices, simple_moving_average, exponential_moving_average

    def format_data(self, crypto_data_dict):
        data = crypto_data_dict['data']
        data['time'] = data['time'].apply(Helper.convert_to_date)
        return data

    def max_close_per_week(self, data):
        df_max_prices = pd.DataFrame(
            data.groupby(data['time'].dt.week, as_index=False).agg({'close': ['max', 'idxmax']}))
        max_prices_indexes = df_max_prices.iloc[:, df_max_prices.columns.get_level_values(1) == 'idxmax'].values
        list_of_indexes = list(itertools.chain(*max_prices_indexes))
        return data.iloc[list_of_indexes]

    def min_close_per_week(self, data):
        df_min_prices = pd.DataFrame(
            data.groupby(data['time'].dt.week, as_index=False).agg({'close': ['min', 'idxmin']}))
        min_prices_indexes = df_min_prices.iloc[:, df_min_prices.columns.get_level_values(1) == 'idxmin'].values
        list_of_indexes = list(itertools.chain(*min_prices_indexes))
        return data.iloc[list_of_indexes]
