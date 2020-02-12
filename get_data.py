import requests
from plyer import notification
import os
from functools import reduce
import datetime

import matplotlib.pyplot as plt

todayBTCPriceURL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
weeklyBTCPricesURL = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=7']]]]]]]]=###=]=]=#=#]=#]=#=#


# Retrieve the current bitcoin price
def get_today_btc_price():
    response = requests.get(todayBTCPriceURL)
    bitcoin_data = response.json()
    bitcoin_price_object = bitcoin_data['USD']
    bitcoin_price_int = int(bitcoin_price_object)
    return '$' + str(bitcoin_price_int)


# Retrieve the weekly average bitcoin price
def weekly_average_btc_price():
    # we don't need the date variable from this variable
    bitcoin_prices, _ = get_weekly_btc_prices()
    average = int(reduce(add_sum, bitcoin_prices)) / len(bitcoin_prices)
    return average


# Retrieve the prices of bitcoin for the past week
def get_weekly_btc_prices():
    weekly_btc_data = get_weekly_btc_data()
    bitcoin_prices = []
    dates = []
    for index, item in enumerate(weekly_btc_data):
        bitcoin_prices.append(int(item['close']))

    for index, item in enumerate(weekly_btc_data):
        timestamp = (int(item['time']))
        dates.append(datetime.datetime.fromtimestamp(timestamp))

    dates = [(date.strftime("%a") + ' ' + str(date.day)) for date in dates]

    return bitcoin_prices, dates


def plot_weekly_btc_prices():
    bitcoin_prices, dates = get_weekly_btc_prices()
    plt.plot(dates, bitcoin_prices, 'go--', color='brown', linewidth=1, markersize=12)
    plt.ylabel('Price of a single bitcoin in dollars')
    plt.xlabel('Days of the week')
    plt.show()\


# Retrieve weekly bitcoin data from API
def get_weekly_btc_data():
    response = requests.get(weeklyBTCPricesURL)
    bitcoin_data = response.json()
    outer_level_data = bitcoin_data['Data']
    inner_level_data = outer_level_data['Data']
    return inner_level_data


# Generic add function which can be supplied to calculate averages
def add_sum(x1, x2):
    return x1 + x2


def initialise_notification():
    bitcoin_price = get_today_btc_price()
    notification.notify(
        title='Current price',
        message=bitcoin_price,
        app_icon=r'C:\Users\menez\PycharmProjects\Stock_Notifier\btc.ico',
        timeout=10,  # seconds
    )


