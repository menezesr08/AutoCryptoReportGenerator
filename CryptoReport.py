# TODO: Decide where to format JSON data
# SubTodos / Notes for this task
# Notes: Difficult to decide so create manager class and see if its too much code
# TODO: Create a class that takes the formatted data and performs operations
# SubTodos for this task
# --------------------------------------------------------------------
# TODO: Decide where to plot your results
# SubTodos for this task
# --------------------------------------------------------------------
# TODO: send email of results
# SubTodos for this task
# --------------------------------------------------------------------
import requests
import json

from CryptoDataModel import CryptoDataModel
from ReportGenerator import ReportGenerator


class CryptoReport:
    def __init__(self, days):
        self.weeklyBTCPricesURL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit={days}'

    # Parse json data to get relevant information
    def parse_json_data(self):
        response = requests.get(self.weeklyBTCPricesURL)
        bitcoin_data = response.json()
        outer_level_data = bitcoin_data['Data']
        inner_level_data = outer_level_data['Data']
        return inner_level_data

    def get_crypto_data(self):
        # returns a list of objects
        json_data = self.parse_json_data()
        btc_data_list = []
        for item in json_data:
            data = CryptoDataModel(item)
            btc_data_list.append(data)

        return btc_data_list

    def create_report(self):
        report = ReportGenerator(self.get_crypto_data())
        report.average_bitcoin_price()


report = CryptoReport(7)
report.create_report()



