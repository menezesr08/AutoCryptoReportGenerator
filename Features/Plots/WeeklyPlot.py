import itertools

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from dateutil.rrule import MO

import Helper
from Features.Plots.BasePlot import BasePlot
from enums.PlotLabels import PlotLabels


class WeeklyPlot(BasePlot):
    def __init__(self, crypto_data_dict, simple_moving_average, exponential_moving_average):
        super().__init__(crypto_data_dict)

        self.sma = simple_moving_average
        self.ema = exponential_moving_average

        self.window = crypto_data_dict['window']

        self.weekly_min_prices, self.weekly_max_prices, self.simple_moving_average, self.exponential_moving_average = \
            self.calculate_statistics(self.formatted_data)

        self.ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=MO))
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%a %d %b'))

    def plot_lines(self):
        self.ax.plot(self.formatted_data['time'], self.formatted_data['close'], marker='', color='orange', linewidth=4,
                     alpha=0.3)
        self.ax.plot(self.formatted_data['time'], self.simple_moving_average, color='red', linewidth=1, alpha=0.5,
                     label="Simple moving average")
        self.ax.plot(self.formatted_data['time'], self.exponential_moving_average, color='blue', linewidth=1, alpha=0.5,
                     label="Exponential moving average")
        self.ax.scatter(self.weekly_max_prices['time'], self.weekly_max_prices['close'], marker=
                        PlotLabels.week_scatter_point.value, color='black',
                        label="Max price for each week")
        self.ax.scatter(self.weekly_min_prices['time'], self.weekly_min_prices['close'], marker=
                        PlotLabels.week_scatter_point.value, color='red',
                        label="Min price for each week")

    def calculate_statistics(self, formatted_data):
        weekly_min_prices = self.min_close_per_week(formatted_data[['time', 'close']])
        weekly_max_prices = self.max_close_per_week(formatted_data[['time', 'close']])
        simple_moving_average = self.sma(formatted_data['close'], self.window.value)
        exponential_moving_average = self.ema(formatted_data['close'], self.window.value)
        return weekly_min_prices, weekly_max_prices, simple_moving_average, exponential_moving_average

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
