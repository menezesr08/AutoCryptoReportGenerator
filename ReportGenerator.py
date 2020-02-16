from functools import reduce

from CryptoDataModel import CryptoDataModel


class ReportGenerator:
    def __init__(self, data):
        self.data = data

    def average_bitcoin_price(self):
        average = []
        price = int(reduce(self.add_two_values, self.data) / len(self.data))
        print(price)

    # making sure we add floats together
    @staticmethod
    def add_two_values(a, b):
        if isinstance(a, CryptoDataModel):
            a = a.close

        if isinstance(b, CryptoDataModel):
            b = b.close

        return a + b

    # Todo: get list of weekly btc prices
