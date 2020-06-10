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
        # self.empty_folder('C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\main\\images')
        # self.empty_folder('C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\main\\pdfs')
        self.api: CryptoReport = CryptoReport(currency, chosen_date)
        # data = self.api.get_crypto_historical_data()
        # self.plot = HistoricalDataPlots(data).create_plot()
        pdf = PDFBuilder()
        pdf.create_historical_data_page()
        pdf.create_trading_signals_page()
        pdf.create_news_page(self.api.get_news_data())
        pdf.document.output('report.pdf')
        # self.plot = TradingSignals(self.api.get_trading_signals()).create_plot()
        # self.news = News(self.api.get_news_data()).create_news_page()

        # self.document = fpdf.FPDF()
        # self.create_pdf()

    def create_pdf(self):
        self.document.add_font("NotoSans", style="B", fname="NotoSans-Bold.ttf", uni=True)
        self.document.add_font("NotoSans", style="I", fname="NotoSans-Italic.ttf", uni=True)
        self.document.add_font("NotoSans", style="BI", fname="NotoSans-BoldItalic.ttf", uni=True)
        self.document.add_font("NotoSans", style="M", fname="NotoSans-Medium.ttf", uni=True)

        # add first plot
        self.document.add_page(orientation="L")
        self.document.image('images/plot - {0}.png'.format(Helper.todays_date()))
        self.document.output('test.pdf')

    def empty_folder(self, folder_path):
        for file_object in os.listdir(folder_path):
            file_object_path = os.path.join(folder_path, file_object)
            if os.path.isfile(file_object_path) or os.path.islink(file_object_path):
                os.unlink(file_object_path)
            else:
                shutil.rmtree(file_object_path)


report: ReportGenerator = ReportGenerator("ETH", chosen_date="month")
