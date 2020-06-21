import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('agg')


class TradingSignals:
    categories = {"inOutVar": "This momentum signal calculates\nhow many addresses are in profit.\nThis is referred"
                              " to as\n'In the money'.",
                  "addressesNetGrowth": "This momentum signal calculates\nhow many addresses are\nbeing created than "
                                        "emptied.",
                  "largetxsVar": "This momentum signal records\nthe number of transactions.",
                  "concentrationVar": "The concentration signal is\n based on the "
                                      "number\nof address with more than\n0.1% of circulating supply"}

    def __init__(self, data):
        self.data = data

    def create_plots(self):
        for key in self.data.keys():
            if key in self.categories.keys():
                trading_signal = self.data[key]
                scores = [trading_signal['score'], 1 - trading_signal['score']]
                labels = ['bullish', 'bearish']
                colors = ['lightskyblue', 'lightcoral']
                explode = (0.1, 0)

                plt.pie(scores, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True,
                        startangle=140)
                plt.title(key, y=1.1, fontweight='bold', fontsize=12)

                plt.axis('equal')
                plt.savefig(f'main/images/{key}_fig.png')
                plt.close()
