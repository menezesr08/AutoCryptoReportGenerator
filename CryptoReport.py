# TODO: Decide where to plot your results
# SubTodos for this task
# --------------------------------------------------------------------
# TODO: send email of results
# SubTodos for this task
# --------------------------------------------------------------------
import requests
import pandas as pd
import json

from CryptoDataModel import CryptoDataModel
import pickle
from requests.exceptions import Timeout

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
    def __init__(self, options):
        self.api_key = '738510752db4953d28dfc15ff4da8812af46d98dd961da115924cc5933ceb808'
        self.list_of_currencies = options

    def get_crypto_historical_data(self) -> list:
        list_crypto_data = []
        for currency in self.list_of_currencies:
            url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={currency}&tsym=USD&limit=7&' \
                  f'api_key={self.api_key}'
            response = requests.get(url).json()
            outer_level = response['Data']
            df = pd.DataFrame(outer_level['Data'])
            df.set_index('time')
            # model = CryptoDataModel(df.to_dict())
            # model.__setattr__('title', currency)
            model = {'title': currency, 'data': df}
            list_crypto_data.append(model)

        pickle.dump(list_crypto_data, open("save.p", "wb"))
        return list_crypto_data

    # # Todo: getting data from api is slow. Difficult to find a fix. Keep researching. (Not important task atm)
    # def get_data_from_api(self):
    #     try:
    #         response = requests.get(self.weeklyBTCPricesURL, timeout=1)
    #     except Timeout:
    #         print('The request timed out')
    #     else:
    #         return response.json()
    #
    # # Parse json data to get relevant information
    # def parse_json_data(self):
    #     bitcoin_data = self.get_data_from_api()
    #     outer_level_data = bitcoin_data['Data']
    #     inner_level_data = outer_level_data['Data']
    #     return inner_level_data
    #
    # def get_crypto_data(self):
    #     # returns a list of objects
    #     json_data = self.parse_json_data()
    #     btc_data_list = []
    #     for item in json_data:
    #         data = CryptoDataModel(item)
    #         btc_data_list.append(data)
    #
    #     return btc_data_list
    #
    # def create_report(self):
    #     report = ReportGenerator(self.get_crypto_data())
    #     report.plot_volumefrom_volumeto_price()
