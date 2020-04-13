import datetime


def add_two_values(a, b):
    return a + b


def format_date(date, pos):
    print(date)
    formatted_date = date.strftime("%b") + ' ' + str(date.day) + ' ' + str(date.year)
    return formatted_date


def convert_to_date(timestamp):
    timestamp = (int(timestamp))
    return datetime.datetime.fromtimestamp(timestamp)


def format_timestamp(time):
    date = convert_to_date(time)
    return format_date(date)


