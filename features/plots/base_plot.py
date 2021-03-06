import matplotlib.pyplot as plt

from main import helper
from enums.plot_labels import PlotLabels
import matplotlib.dates as mdates
from main.utils import get_project_root
import os


class BasePlot:
    def __init__(self, crypto_data_dict):
        self.ax, self.fig = self.initialise_plot()
        self.formatted_data = self.format_data(crypto_data_dict['data'])
        self.title = crypto_data_dict['title']
        self.time_period = crypto_data_dict['time_period']

        self.ax.xaxis.set_major_locator(mdates.DayLocator())
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
        self.ax.patch.set_edgecolor('black')
        self.ax.patch.set_linewidth('1')

        self.root = str(get_project_root())

    def create_plot(self):
        self.plot_lines()
        # self.apply_labels()
        self.apply_legend()
        path = os.path.join(self.root, 'images/historical_fig.png')
        plt.savefig(path)
        plt.close()

    def initialise_plot(self):
        plt.style.use('seaborn-darkgrid')
        my_dpi = 150
        fig = plt.figure(figsize=(10, 10), dpi=my_dpi)
        ax = fig.add_subplot(111)
        ax.grid(True)
        return ax, fig

    def plot_lines(self):
        self.ax.plot(self.formatted_data['time'], self.formatted_data['close'], marker='', color='orange', linewidth=4,
                     alpha=0.3, label=PlotLabels.crypto_label.value.format(self.title))

    def format_data(self, data):
        data['time'] = data['time'].apply(helper.convert_to_date)
        return data

    def apply_labels(self):
        self.ax.set_xlabel(PlotLabels.x_label.value)
        self.ax.set_ylabel(PlotLabels.y_label.value.format(self.title))
        self.ax.xaxis.labelpad = 40
        self.ax.yaxis.labelpad = 40

    def apply_legend(self):
        box = self.ax.get_position()
        legend_prop = {'family': 'Times New Roman'}

        self.ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        # Put a legend to the right of the current axis
        self.ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),
                       labelspacing=2, prop=legend_prop)
