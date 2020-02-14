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


class ReportGenerator:
    def __init__(self, days):
        self.weeklyBTCPricesURL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit={days}'

    def get_weekly_btc_data(self):
        response = requests.get(self.weeklyBTCPricesURL)
        bitcoin_data = response.json()
        outer_level_data = bitcoin_data['Data']
        inner_level_data = outer_level_data['Data']
        return inner_level_data

    def format_data(self):
        # returns a list of objects
        json_data = self.get_weekly_btc_data()
        btc_data_daily_list = []


generator = ReportGenerator(7)

print(generator.format_data())
