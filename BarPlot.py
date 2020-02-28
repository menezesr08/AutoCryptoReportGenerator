import matplotlib.pyplot as plt


class BarPlot:
    def __init__(self, first_data_set, second_data_set, dates, color, label):
        self.first_data_set = first_data_set
        self.second_data_set = second_data_set
        self.dates = dates
        self.color = color
        self.width = 0.35
        self.label = label

    def plot_data(self):
        plt.style.use('fivethirtyeight')
        x_indexes = np.arange(len(self.dates))
        plt.bar(x_indexes - (self.width / 2), self.first_data_set, width=self.width, label=self.label)
        plt.bar(x_indexes + (self.width / 2), self.second_data_set, width=self.width, color=self.color,
                label=self.label)
        plt.legend()
        plt.xticks(ticks=x_indexes, labels=self.dates)

    # Todo: adding too many parameters in constructor. Need to think of different approach
