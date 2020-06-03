import fpdf

import Helper
from Features.HistoricalDataPlots import HistoricalDataPlots
from Features.TradingSignals import TradingSignals
from main.API import CryptoReport
from Features.News import News


class ReportGenerator:
    fpdf.set_global("SYSTEM_TTFONTS", 'C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\fonts')

    def __init__(self, currency, chosen_date):
        self.api: CryptoReport = CryptoReport(currency, chosen_date)
        self.plot = HistoricalDataPlots(self.api.get_crypto_historical_data()).create_plot()
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


report: ReportGenerator = ReportGenerator("BTC", chosen_date="month")
