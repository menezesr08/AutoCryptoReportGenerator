class LinePlot:
    line_width = 1
    marker_size = 8

    @classmethod
    def plot_historical_data(cls, title, data):
        new_dataset = data[['time', 'close']]

        # new_dataset.loc['time'] = new_dataset['time'].apply(Helper.convert_to_date)
        # new_dataset = new_dataset.set_index('time')
        # new_dataset.index = pd.to_datetime(new_dataset.index, unit='s')
        # new_dataset.groupby(pd.Grouper(freq='M'))
        # print(new_dataset.head())
        # # print(plotted_data.head)
        # # close_prices = data['close']
        # # close_prices.index = data['time'].apply(Helper.format_timestamp)
        # #
        # # plt.plot(plotted_data['time'], plotted_data['close'])
        # # ax = close_prices.plot(color=[color.value for color in CryptoColors if str(color.name) is title],
        # #                markersize=cls.marker_size)
        # #
        # # ax.set_xlabel('Years')
        # # ax.set_ylabel(f'Price of a single {title}')
        #
        # # plt.plot(data['time'].apply(Helper.convert_to_date).dt.strftime('%d'), data['close'])
        #
        # df = pd.DataFrame(data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.idxmax())
        # df['price'] = data.groupby(data['time'].apply(Helper.convert_to_date).dt.month).close.max()
        # plt.scatter(df['close'], df['price'])
        # max_values = data.groupby(pd.to_datetime(data['time'].apply(Helper.convert_to_date).dt.month)[['close']].max())
        # print(max_values.head())
        #
        # # max_dates = max_values.merge(max_values, how='inner')
        # # print(max_values)
        # # print(max_dates)
        #
        # # plt.scatter(max_values.index, max_values)
        # # plt.xticks(rotation=45)
        # plt.show()
        # Todo: focus on design of each plot
