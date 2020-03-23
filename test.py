import get_data

import matplotlib.pyplot as plt

import datetime
#
import requests
import urllib.request
import pandas as pd

api_key = '738510752db4953d28dfc15ff4da8812af46d98dd961da115924cc5933ceb808'
payload = {
    "api_key": api_key,
    "fsym": "BTC",
    "tsym": "USD",
    "limit": 10
}

url = "https://min-api.cryptocompare.com/data/histoday"


def load_multiple(*args):
    crypto_data = []
    for currency in args:
        payload["fsym"] = currency
        response = requests.get(url, params=payload).json()
        df = pd.DataFrame(response['Data'])
        crypto_data.append(df)

    return crypto_data


data = load_multiple("BTC", "ETH");
print(data)
