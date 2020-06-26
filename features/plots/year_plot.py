import itertools

import matplotlib.dates as mdates
import pandas as pd

from features.plots.base_plot import BasePlot
from enums.plot_labels import PlotLabels


class YearPlot(BasePlot):

    def __init__(self, crypto_data_dict, simple_moving_average, exponential_moving_average):
        super().__init__(crypto_data_dict)
        self.plot_period = "year"
        self.title = crypto_data_dict["title"]
        self.window = crypto_data_dict['window']

        self.sma = simple_moving_average
        self.ema = exponential_moving_average

        self.yearly_min_prices, self.yearly_max_prices, self.simple_moving_average, self.exponential_moving_average = \
            self.calculate_statistics(self.formatted_data)

        self.ax.xaxis.set_major_locator(mdates.YearLocator())
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    def plot_lines(self):
        self.ax.plot(self.formatted_data['time'],
                     self.formatted_data['close'], color=PlotLabels.crypto_color.value,
                     linewidth=PlotLabels.crypto_linewidth.value,
                     alpha=PlotLabels.crypto_alpha.value,
                     label=PlotLabels.crypto_label.value.format(self.title))

        self.ax.plot(self.formatted_data['time'],
                     self.simple_moving_average,
                     color=PlotLabels.sma_color.value,
                     linewidth=PlotLabels.sma_linewidth.value,
                     alpha=PlotLabels.sma_alpha.value,
                     label=PlotLabels.sma_label.value)

        self.ax.plot(self.formatted_data['time'],
                     self.exponential_moving_average,
                     color=PlotLabels.ema_color.value,
                     linewidth=PlotLabels.ema_linewidth.value,
                     alpha=PlotLabels.ema_alpha.value,
                     label=PlotLabels.ema_label.value)

        self.ax.scatter(self.yearly_max_prices['time'],
                        self.yearly_max_prices['close'],
                        marker=PlotLabels.week_scatter_point.value,
                        color=PlotLabels.scatter_color_max.value,
                        label=PlotLabels.scatter_label_max.value.format(self.title, self.plot_period))

        self.ax.scatter(self.yearly_min_prices['time'],
                        self.yearly_min_prices['close'],
                        marker=PlotLabels.week_scatter_point.value,
                        color='red',
                        label=PlotLabels.scatter_label_min.value.format(self.title, self.plot_period))

        self.fig.autofmt_xdate()

    def calculate_statistics(self, formatted_data):
        yearly_min_prices = self.min_close_per_year(formatted_data[['time', 'close']])
        yearly_max_prices = self.max_close_per_year(formatted_data[['time', 'close']])
        simple_moving_average = self.sma(formatted_data['close'], self.window.value)
        exponential_moving_average = self.ema(formatted_data['close'], self.window.value)
        return yearly_min_prices, yearly_max_prices, simple_moving_average, exponential_moving_average

    def max_close_per_year(self, data):
        df_max_prices = pd.DataFrame(
            data.groupby(data['time'].dt.year, as_index=False).agg({'close': ['max', 'idxmax']}))
        max_prices_indexes = df_max_prices.iloc[:, df_max_prices.columns.get_level_values(1) == 'idxmax'].values
        list_of_indexes = list(itertools.chain(*max_prices_indexes))
        return data.iloc[list_of_indexes]

    def min_close_per_year(self, data):
        df_min_prices = pd.DataFrame(
            data.groupby(data['time'].dt.year, as_index=False).agg({'close': ['min', 'idxmin']}))
        min_prices_indexes = df_min_prices.iloc[:, df_min_prices.columns.get_level_values(1) == 'idxmin'].values
        list_of_indexes = list(itertools.chain(*min_prices_indexes))
        return data.iloc[list_of_indexes]
