import datetime


def add_two_values(a, b):
    return a + b


def format_date(date):
    formatted_date = date.strftime("%a") + ' ' + str(date.day)
    return formatted_date


def get_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)
