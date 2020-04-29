from enum import Enum

from enums.Limits import Limits
from enums.TimePeriod import TimePeriod
from enums.WindowSize import WindowSize


class ConfigOptions(Enum):
    week = (Limits.WEEK, TimePeriod.WEEK, WindowSize.WEEK)
    month = (Limits.MONTH, TimePeriod.WEEK, WindowSize.MONTH)
    three_months = (Limits.THREE_MONTHS, TimePeriod.MONTH, WindowSize.THREE_MONTHS)
    six_months = (Limits.SIX_MONTHS, TimePeriod.MONTH, WindowSize.SIX_MONTHS)
    year = (Limits.YEAR, TimePeriod.MONTH, WindowSize.YEAR)
    three_years = (Limits.THREE_YEARS, TimePeriod.YEAR, WindowSize.THREE_YEARS)
    five_years = (Limits.FIVE_YEARS, TimePeriod.YEAR, WindowSize.FIVE_YEARS)
