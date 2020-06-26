import os
import shutil

import fpdf

import Helper
from Features.HistoricalDataPlots import HistoricalDataPlots
from Features.TradingSignals import TradingSignals
from main.API import CryptoReport
from main.EmailSender import EmailSender

from main.PDFBuilder import PDFBuilder


class ReportGenerator:
    fpdf.set_global("SYSTEM_TTFONTS", 'C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\fonts')

    def __init__(self, currency, chosen_date, receiver_email):
        # self.empty_folder('C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\main\\images')
        # self.empty_folder('C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\main\\pdfs')
        self.currency = currency
        self.chosen_date = chosen_date
        self.receiver_email = receiver_email
        self.pdf = PDFBuilder()

    def get_data_from_api(self):
        api = CryptoReport(self.currency, self.chosen_date)
        historical_data = api.get_crypto_historical_data()
        trading_data = api.get_trading_signals()
        news_data = api.get_news_data()
        return historical_data, trading_data, news_data

    def generate_report(self):
        historical_data, trading_data, news_data = self.get_data_from_api()
        self.historical_data_pdf(historical_data)
        self.trading_data_pdf(trading_data)
        self.news_data_pdf(news_data)
        self.pdf.document.output('pdfs/report.pdf')
        EmailSender(self.receiver_email).send_email()

    def historical_data_pdf(self, historical_data):
        HistoricalDataPlots(historical_data).create_plot()
        title = historical_data['title']
        time_period = historical_data['time_period'].value
        self.pdf.create_historical_data_page(title, time_period)

    def trading_data_pdf(self, trading_data):
        TradingSignals(trading_data).create_plots()
        self.pdf.create_trading_signals_page()

    def news_data_pdf(self, news_data):
        self.pdf.create_news_page(news_data)

    # def empty_folder(self, folder_path):
    #     for file_object in os.listdir(folder_path):
    #         file_object_path = os.path.join(folder_path, file_object)
    #         if os.path.isfile(file_object_path) or os.path.islink(file_object_path):
    #             os.unlink(file_object_path)
    #         else:
    #             shutil.rmtree(file_object_path)


report: ReportGenerator = ReportGenerator("ETH", "three_months", "menezesr08@gmail.com")
report.generate_report()
