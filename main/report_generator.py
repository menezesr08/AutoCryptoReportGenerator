from features.historical_data_plots import HistoricalDataPlots
from features.trading_signals import TradingSignals
from main.api import CryptoReport
from main.email_sender import EmailSender
from main.pdf_builder import PDFBuilder


class ReportGenerator:

    def __init__(self, currency, chosen_date, receiver_email):
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
        self.build_historical_data(historical_data)
        self.build_trading_signals(trading_data)
        self.build_news_page(news_data)
        self.pdf.save_pdf_file()
        self.send_report()

    def build_historical_data(self, historical_data):
        HistoricalDataPlots(historical_data).create_plot()
        title = historical_data['title']
        time_period = historical_data['time_period'].value
        self.pdf.create_historical_data_page(title, time_period)

    def build_trading_signals(self, trading_data):
        TradingSignals(trading_data).create_plots()
        self.pdf.create_trading_signals_page()

    def build_news_page(self, news_data):
        self.pdf.create_news_page(news_data)

    def send_report(self):
        EmailSender(self.receiver_email).send_email()


#
report = ReportGenerator("BTC", "year", "velatrix0@gmail.com")
report.generate_report()
