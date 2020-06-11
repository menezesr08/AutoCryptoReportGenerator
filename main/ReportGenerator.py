import os
import shutil

import fpdf

import Helper
from Features.HistoricalDataPlots import HistoricalDataPlots
from Features.TradingSignals import TradingSignals
from main.API import CryptoReport

from main.PDFBuilder import PDFBuilder


class ReportGenerator:
    fpdf.set_global("SYSTEM_TTFONTS", 'C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\fonts')

    def __init__(self, currency, chosen_date):
        self.empty_folder('C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\main\\images')
        # self.empty_folder('C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\main\\pdfs')
        self.api: CryptoReport = CryptoReport(currency, chosen_date)
        historical_data = self.api.get_crypto_historical_data()
        HistoricalDataPlots(historical_data).create_plot()
        trading_data = self.api.get_trading_signals()
        TradingSignals(trading_data).create_plots()
        pdf = PDFBuilder()
        title = historical_data['title']
        time_period = historical_data['time_period'].value
        pdf.create_historical_data_page(title, time_period)
        pdf.create_trading_signals_page()
        pdf.create_news_page(self.api.get_news_data())
        pdf.document.output('pdfs/report.pdf')

    def empty_folder(self, folder_path):
        for file_object in os.listdir(folder_path):
            file_object_path = os.path.join(folder_path, file_object)
            if os.path.isfile(file_object_path) or os.path.islink(file_object_path):
                os.unlink(file_object_path)
            else:
                shutil.rmtree(file_object_path)


report: ReportGenerator = ReportGenerator("BTC", chosen_date="three_months")
