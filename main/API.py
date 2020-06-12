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
        self.currency = options
        self.chosen_date = chosen_date
        self.limit, self.time_period, self.window_size = \
            [option.value for option in ConfigOptions if str(option.name) is
             chosen_date][0]

    def get_crypto_historical_data(self):
        url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={self.currency}&tsym=USD&limit={self.limit.value}&' \
              f'api_key={self.api_key}'
        response = requests.get(url).json()
        outer_level = response['Data']
        df = pd.DataFrame(outer_level['Data'])
        df.set_index('time')
        model = {'title': self.currency, 'data': df, 'time_period': self.time_period, 'window': self.window_size}

        pickle.dump(model, open("../save.p", "wb"))
        return model

    def get_news_data(self):
        url = f'https://min-api.cryptocompare.com/data/v2/news/?categories={self.currency},Mining,Technology'
        response = requests.get(url).json()
        data = response['Data'][:5]
        pickle.dump(data, open("../save.p", "wb"))
        return data

    def get_trading_signals(self):
        url = f'https://min-api.cryptocompare.com/data/tradingsignals/intotheblock/latest?fsym={self.currency}'
        response = requests.get(url).json()
        data = response['Data']
        return data

    @staticmethod
    def get_api_key():
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['API']['KEY']
