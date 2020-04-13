from CryptoDataModel import CryptoDataModel
from CryptoReport import CryptoReport
from HistoricalDataPlots import HistoricalDataPlots
import pickle
import pandas as pd
from Plots.BarPlot import BarPlot
import Helper
from Plots.DoubleLinePlot import DoubleLinePlot
from Plots.LinePlot import LinePlot


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
    def __init__(self, *options: str):
        # 'options' has type 'Tuple[str, str...]' (a type of strings)
        self.options: list = [option for option in options]
        self.api: CryptoReport = CryptoReport(self.options)
        data = pickle.load(open("save.p", "rb"))
        HistoricalDataPlots(data).create_plots()


report: ReportGenerator = ReportGenerator("BTC")
