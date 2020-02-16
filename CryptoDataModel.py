# Attributes
# -----------------------------------------------
# close, conversionSymbol, conversionType, high, low, open, time, volumefrom, volumeto


class CryptoDataModel:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)
