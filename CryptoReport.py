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
from requests.exceptions import Timeout


class CryptoReport:
    def __init__(self, days):
        self.api_key = '738510752db4953d28dfc15ff4da8812af46d98dd961da115924cc5933ceb808'
        self.weeklyBTCPricesURL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit={days}&api_key={self.api_key}'

    # Todo: fix this method
    def get_data_from_api(self):
        try:
            response = requests.get(self.weeklyBTCPricesURL, timeout=1)
        except Timeout:
            print('The request timed out')
        else:
            return response.json

    # Parse json data to get relevant information
    def parse_json_data(self):
        bitcoin_data = self.get_data_from_api()
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
        print(report.get_all_prices())


report = CryptoReport(1)
report.create_report()



