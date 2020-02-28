import matplotlib.pyplot as plt


class LinePlot:
    def __init__(self, dates, data, color):
        self.data = data
        self.dates = dates
        self.color = color
        self.line_width = 1
        self.marker_size = 8

    def plot_data(self):
        plt.plot(self.dates, self.data, 'go--', color=self.color, linewidth=self.line_width, markersize=self.marker_size)
        plt.ylabel('Price of a single bitcoin in dollars')
        plt.xlabel('Days of the week')
        plt.show()
