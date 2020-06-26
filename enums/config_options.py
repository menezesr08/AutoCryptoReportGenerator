from enum import Enum

from enums.limits import Limits
from enums.time_period import TimePeriod
from enums.window_size import WindowSize


class ConfigOptions(Enum):
    week = (Limits.WEEK, TimePeriod.seven_days, None)
    month = (Limits.MONTH, TimePeriod.month, WindowSize.MONTH)
    three_months = (Limits.THREE_MONTHS, TimePeriod.three_months, WindowSize.THREE_MONTHS)
    six_months = (Limits.SIX_MONTHS, TimePeriod.six_months, WindowSize.SIX_MONTHS)
    year = (Limits.YEAR, TimePeriod.year, WindowSize.YEAR)
    three_years = (Limits.THREE_YEARS, TimePeriod.three_months, WindowSize.THREE_YEARS)
    five_years = (Limits.FIVE_YEARS, TimePeriod.five_years, WindowSize.FIVE_YEARS)
