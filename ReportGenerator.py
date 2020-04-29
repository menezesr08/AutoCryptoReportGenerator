from API import CryptoReport
from Plots.HistoricalDataPlots import HistoricalDataPlots


#
#     def get_all_dates(self):
#         dates = []
#         for item in self.data:
#             timestamp = (int(item.time))
#             dates.append(Helper.get_date(timestamp))
#
#         dates = [Helper.format_date(date) for date in dates]
#         return dates


class ReportGenerator:
    def __init__(self, *options: str, chosen_date):
        # 'options' has type 'Tuple[str, str...]' (a type of strings)
        self.options: list = [option for option in options]
        self.api: CryptoReport = CryptoReport(self.options, chosen_date)
        # data = pickle.load(open("save.p", "rb"))
        HistoricalDataPlots(self.api.get_crypto_historical_data()).create_plots()


report: ReportGenerator = ReportGenerator("BTC", chosen_date="month")
