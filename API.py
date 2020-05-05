# TODO: Decide where to plot your results
# SubTodos for this task
# --------------------------------------------------------------------
# TODO: send email of results
# SubTodos for this task
# --------------------------------------------------------------------
import requests
import pandas as pd

import pickle
import configparser

from enums.ConfigOptions import ConfigOptions

'''
The API url takes in a some parameters: 
- currency: the cryptocurrency chosen by the user
- limit: the number of records to return. By default the data is returned per day. So limit = 10 means previous 10 days
- aggregrate: How far apart you want the data. For example if limit = 30 and aggregate = 3, then we are asking the api
  to return data from 90 days ago spread out in intervals of 3 days. (30 x 3 = 90), hence the data would return 30 
  records.
- toTs: you can return historical data from this timestamp. Might be useful for really old data
  
'''


class CryptoReport:
    def __init__(self, options, chosen_date):
        self.api_key = self.get_api_key()
        self.list_of_currencies = options
        self.chosen_date = chosen_date
        self.limit, self.time_period, self.window_size = \
            [option.value for option in ConfigOptions if str(option.name) is
             chosen_date][0]

    # self.time_period = [time_period for time_period in TimePeriods if str(time_period.name) is chosen_date]

    def get_crypto_historical_data(self) -> list:
        list_crypto_data = []
        for currency in self.list_of_currencies:
            url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={currency}&tsym=USD&limit={self.limit.value}&' \
                  f'api_key={self.api_key}'
            response = requests.get(url).json()
            outer_level = response['Data']
            df = pd.DataFrame(outer_level['Data'])
            df.set_index('time')
            model = {'title': currency, 'data': df, 'time_period': self.time_period, 'window': self.window_size}
            list_crypto_data.append(model)

        pickle.dump(list_crypto_data, open("save.p", "wb"))
        return list_crypto_data

    def get_news_data(self):
        url = 'https://min-api.cryptocompare.com/data/v2/news/?categories=BTC,ETH,XRP,Mining,Technology'
        response = requests.get(url).json()

    def get_trading_signals(self):
        url = 'https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest?fsym=BTC'
        response = requests.get(url).json()
        data = response['Data']
        return data

    @staticmethod
    def get_api_key():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['API']['KEY']
