import get_data

import matplotlib.pyplot as plt

import datetime

bitcoin_prices, dates = get_data.get_weekly_btc_prices()
plt.plot(dates, bitcoin_prices, 'go--', color='brown', linewidth=1, markersize=12)
plt.ylabel('Price of a single bitcoin in dollars')
plt.xlabel('Days of the week')

plt.show()
from functools import reduce


def add_sum(x1, x2):
    return x1 + x2


bitcoin_prices = [1, 2, 3, 4, 5]

average = int(reduce(add_sum, bitcoin_prices)) / len(bitcoin_prices)
