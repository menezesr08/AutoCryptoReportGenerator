import itertools

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from dateutil.rrule import MO

import Helper
from enums.PlotLabels import PlotLabels


class WeeklyPlot:

    def __init__(self, crypto_data_dict, simple_moving_average, exponential_moving_average):
        self.title = crypto_data_dict['title']
        self.window = crypto_data_dict['window']

        self.sma = simple_moving_average
        self.ema = exponential_moving_average

        self.formatted_data = self.format_data(crypto_data_dict['data'])
        self.weekly_min_prices, self.weekly_max_prices, self.simple_moving_average, self.exponential_moving_average = \
            self.calculate_statistics(self.formatted_data)

        self.ax, self.fig = self.initialise_plot()

    def create_plot(self):
        self.plot_lines()
        self.apply_labels()
        self.apply_legend()
        plt.show()
        # plt.savefig('images/plot - {0}'.format(Helper.todays_date()))

    def initialise_plot(self):
        plt.style.use('seaborn-darkgrid')
        my_dpi = 96
        fig = plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)
        ax = fig.add_subplot(111)
        ax.grid(True)
        ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=MO))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%a %d %b'))
        return ax, fig

    def plot_lines(self):
        self.ax.plot(self.formatted_data['time'], self.formatted_data['close'], marker='', color='orange', linewidth=4,
                     alpha=0.3)
        self.ax.plot(self.formatted_data['time'], self.simple_moving_average, color='red', linewidth=1, alpha=0.5,
                     label="Simple moving average")
        self.ax.plot(self.formatted_data['time'], self.exponential_moving_average, color='blue', linewidth=1, alpha=0.5,
                     label="Exponential moving average")
        self.ax.scatter(self.weekly_max_prices['time'], self.weekly_max_prices['close'], marker="^", color='black',
                        label="Max price for each week")
        self.ax.scatter(self.weekly_min_prices['time'], self.weekly_min_prices['close'], marker="v", color='red',
                        label="Min price for each week")
        self.fig.autofmt_xdate()

    def apply_labels(self):
        self.ax.set_title(PlotLabels.monthly_plot_title.value)
        self.ax.set_xlabel(PlotLabels.monthly_plot_x.value)
        self.ax.set_ylabel(PlotLabels.y_title.value)
        self.ax.xaxis.labelpad = 40
        self.ax.yaxis.labelpad = 4

    def apply_legend(self):
        box = self.ax.get_position()
        self.ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # Put a legend to the right of the current axis
        self.ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    def calculate_statistics(self, formatted_data):
        weekly_min_prices = self.min_close_per_week(formatted_data[['time', 'close']])
        weekly_max_prices = self.max_close_per_week(formatted_data[['time', 'close']])
        simple_moving_average = self.sma(formatted_data['close'], self.window.value)
        exponential_moving_average = self.ema(formatted_data['close'], self.window.value)
        return weekly_min_prices, weekly_max_prices, simple_moving_average, exponential_moving_average

    def format_data(self, data):
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
