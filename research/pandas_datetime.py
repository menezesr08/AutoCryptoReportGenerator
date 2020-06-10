import pandas as pd
from datetime import datetime

# convert to datetime directly as the data is loaded in
d_parser = lambda x: datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)
df['DayOfWeek'] = df['Date'].dt.day_name()
filt = (df['Date'] >= '2019') & (df['Date'] < '2020')
print(df.loc[filt])

