# Attributes
# -----------------------------------------------
# close, conversionSymbol, conversionType, high, low, open, time, volumefrom, volumeto
import datetime
import Helper


class CryptoDataModel:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

    def __str__(self):
        date = Helper.get_date(getattr(self, "time"))
        formatted_date = Helper.format_date(date)
        return f"Crypto data - {formatted_date}"
