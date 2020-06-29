from features.plots.base_plot import BasePlot
from features.plots.month_plot import MonthPlot
from features.plots.week_plot import WeekPlot
from features.plots.year_plot import YearPlot

# testing
class HistoricalDataPlots:
    def __init__(self, data):
        self.data = data
        self.choices = {"7 days": BasePlot,
                        "30 days": WeekPlot,
                        "3 months": MonthPlot,
                        "6 months": MonthPlot,
                        "12 months": MonthPlot,
                        "3 years": YearPlot,
                        "5 years": YearPlot}

    def create_plot(self):
        time_period = self.data['time_period']
        plot_type = self.execute_plot(time_period)

        if plot_type is BasePlot:
            plot = plot_type(self.data)
        else:
            plot = plot_type(self.data, self.calculate_simple_moving_average, self.simple_moving_average)

        plot.create_plot()

    def execute_plot(self, time_period):
        return self.choices.get(time_period.value)

    @staticmethod
    def simple_moving_average(data, window_size):
        short_rolling = data.ewm(span=window_size, adjust=False).mean()
        return short_rolling

    @staticmethod
    def calculate_simple_moving_average(data, window_size):
        short_rolling = data.rolling(window=window_size, min_periods=1).mean()
        return short_rolling
