import get_data

import matplotlib.pyplot as plt

import datetime
#
# import requests
# import urllib.request
# from pandas.json.no
# import pandas as pd
#
# api_key = '738510752db4953d28dfc15ff4da8812af46d98dd961da115924cc5933ceb808'
# weeklyBTCPricesURL = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=8&api_key={api_key}'
# response = requests.get(weeklyBTCPricesURL, timeout=1)
#
# df = pd.DataFrame.from_dict(json_normalize(response.json), orient='columns')
# print(df)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return self.age + other.age
