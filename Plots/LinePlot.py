import matplotlib.pyplot as plt

from CryptoColors import CryptoColors


class LinePlot:
    line_width = 1
    marker_size = 8

    @classmethod
    def plot_historical_data(cls, title, data):
        ax = data.plot(color=[color.value for color in CryptoColors if str(color.name) is title],
                       linewidth=cls.line_width,
                       markersize=cls.marker_size)
        ax.set_xlabel('Years')
        ax.set_ylabel(f'Price of a single {title}')
        plt.xticks(rotation=45)
        plt.show()
