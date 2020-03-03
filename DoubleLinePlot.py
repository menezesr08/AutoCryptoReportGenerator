from LinePlot import LinePlot
import matplotlib.pyplot as plt


class DoubleLinePlot(LinePlot):
    def __init__(self, dates, first_data_set, second_data_set):
        super().__init__(dates, first_data_set)
        self.second_data_set = second_data_set

    # finish this method. Look at different subplots
    def plot_volumefrom_volumeto_prices(self):
        fig, (ax1, ax2) = plt.subplots(2)
        fig.suptitle('Vertically stacked subplots')
        ax1.plot(self.dates, self.data, 'go--', color='brown', linewidth=self.line_width,
                 markersize=self.marker_size)
        ax1.set_xlabel('Days of the week')
        ax1.set_ylabel('Volume at the start of the day')
        ax2.plot(self.dates, self.second_data_set, 'go--', color='brown', linewidth=self.line_width,
                 markersize=self.marker_size)
        # Todo: need to convert the y axis to a more readable format. You need to pass the original set of numbers
        #  but change the yticks to the more readable format
        ax2.set_xlabel('Days of the week')
        ax2.set_ylabel('Volume at the end of the day')
        plt.show()
