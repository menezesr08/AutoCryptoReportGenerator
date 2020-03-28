import datetime


def add_two_values(a, b):
    return a + b


def format_date(date):
    formatted_date = date.strftime("%b") + ' ' + str(date.day)
    return formatted_date


def convert_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)


def format_timestamp(time):
    timestamp = (int(time))
    date = convert_to_date(timestamp)
    return format_date(date)
