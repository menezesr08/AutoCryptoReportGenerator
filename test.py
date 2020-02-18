import get_data

import matplotlib.pyplot as plt

import datetime

import requests
import urllib.request

weeklyBTCPricesURL = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=10'
with urllib.request.urlopen(weeklyBTCPricesURL) as response:
    html = response.read()
    print(html)
