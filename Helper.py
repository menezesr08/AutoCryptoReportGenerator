import datetime
from datetime import datetime


def format_date(date):
    formatted_date = date.strftime("%b") + ' ' + str(date.day) + ' ' + str(date.year)
    return formatted_date


# creates a date object from given timestamp
def convert_to_date(timestamp):
    timestamp = int(timestamp)
    return datetime.fromtimestamp(timestamp)


# For weekly time periods, we format the given date to a more human readable format of DAY / MONTH
def format_month_for_day(date):
    formatted_date = date.strftime("%a %d %b, %Y")
    return formatted_date


# we use this function when creating the name of the output file
def todays_date():
    return datetime.today().strftime('%Y%m%d')
