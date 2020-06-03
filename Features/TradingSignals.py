import matplotlib.pyplot as plt


class TradingSignals:
    categories = {"inOutVar": "Net change of value in addresses",
                  "addressesNetGrowth": "New addresses created",
                  "largetxsVar": "Bitcoin transactions",
                  "concentrationVar": "Number of address with more than 0.1% of circulating supply"}

    def __init__(self, data):
        self.data = data

    def plot_trading_signals(self):
        for key in self.data.keys():
            if key in self.categories.keys():

                address_in_profit = self.data[key]
                scores = [address_in_profit['score'], 1 - address_in_profit['score']]
                labels = ['bullish', 'bearish']
                colors = ['lightskyblue', 'lightcoral']
                explode = (0.1, 0)

                plt.pie(scores, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True,
                        startangle=140)
                plt.title(self.categories[key])

                plt.axis('equal')
                plt.show()