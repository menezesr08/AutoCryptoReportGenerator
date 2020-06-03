# import pickle
# import matplotlib as plt
# import pandas as pd
#
import Helper
#
import pickle
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import itertools

infile = open('save.p', 'rb')
data = pickle.load(infile)
data = data['data']
data['time'] = data['time'].apply(Helper.convert_to_date)
x = data['time']
y = data['close']

data_max = data[['time', 'close']]

df_max_prices = pd.DataFrame(
    data.groupby(data_max['time'].dt.week, as_index=False).agg({'close': ['max', 'idxmax']}))

indexes = df_max_prices.iloc[:, df_max_prices.columns.get_level_values(1) == 'idxmax'].values
flattened_list  = list(itertools.chain(*indexes))
print(data.iloc[flattened_list])
# print indexes. You get a list of list of values. Combine into one list and then use these indexes to subset
# dataframe data

# df_max_prices['id'] = data.groupby(data['time'].dt.week).close.idxmax()


# max_close = df_max_prices['close'].values
#
# closed_value = data.loc[data['close'].isin(max_close)]
# print(data.index)
#
# df_min_prices = pd.DataFrame(
#     data.groupby(data['time'].dt.week).close.min())
#
# min_prices = df_min_prices['close'].values
# min_prices = data.loc[data['close'].isin(min_prices)]
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
#
# ax.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
# ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%a %d %b'))
# ax.plot(x, y)
# ax.scatter(closed_value['time'], closed_value['close'], marker="^", color='blue')
# ax.scatter(min_prices['time'], min_prices['close'], marker="^", color='red')
# fig.autofmt_xdate()
# ax.grid(True)
# #
# plt.show()

