from fpdf import fpdf

from Features.TradingSignals import TradingSignals

from html import unescape


class PDFBuilder:
    fpdf.set_global("SYSTEM_TTFONTS", 'C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\fonts')

    def __init__(self):
        self.document = fpdf.FPDF()
        self.add_global_fonts()

    def add_global_fonts(self):
        self.document.add_font("NotoSans", style="B", fname="NotoSans-Bold.ttf", uni=True)
        self.document.add_font("NotoSans", style="I", fname="NotoSans-Italic.ttf", uni=True)
        self.document.add_font("NotoSans", style="BI", fname="NotoSans-BoldItalic.ttf", uni=True)
        self.document.add_font("NotoSans", style="M", fname="NotoSans-Medium.ttf", uni=True)
        self.document.add_font("NotoSans", style="TI", fname="NotoSans-ThinItalic.ttf", uni=True)
        self.document.add_font("NotoSans", style="CI", fname="NotoSans-ExtraCondensedItalic.ttf", uni=True)
        self.document.add_font("NotoSans", style="LI", fname="NotoSans-LightItalic.ttf", uni=True)
        self.document.add_font("NotoSans", style="TI", fname="NotoSans-ThinItalic.tff", uni=True)

    def create_historical_data_page(self):
        self.document.add_page('L')
        self.add_main_title('BTC prices for the last 3 years')
        self.add_key_terms()

        self.add_section_title('Simple Moving Average', 14)
        self.add_section_body('This is a calculation that averages prices over a period of time and plots '
                              'that average as a line.', 12)

        self.add_section_title('Exponential Moving Average', 14)
        self.add_section_body('This is a type of weighted moving average and gives more importance to recent prices',
                              12)

        image = 'C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\main\\images\\historical_fig.png'
        self.document.image(image, x=10, y=80, w=230, h=130)

    def create_trading_signals_page(self):
        self.document.add_page('L')
        self.add_main_title('Trading Signals')
        self.add_key_terms()
        categories = TradingSignals.categories
        for title, text in categories.items():
            self.add_section_title(title, 14)
            self.add_section_body(text, 12)

    def create_news_page(self, data):
        self.document.add_page('P')
        self.add_main_title('News')

        for article in data:
            self.add_section_title(article['title'], 16)
            self.add_section_body(article['body'], 14)
            self.add_section_source(article['source'])
            self.add_section_url(article['url'])
            self.document.ln()
            self.document.ln()

    def add_main_title(self, title):
        self.document.set_font('NotoSans', 'B', 16)
        self.document.multi_cell(0, 5, title, align='C')
        self.document.ln()
        self.document.ln()

    def add_key_terms(self):
        self.document.set_font('NotoSans', 'M', 14)
        self.document.multi_cell(0, 5, 'Key Terms')
        self.document.ln()

    def add_section_title(self, title, font_size):
        self.document.set_text_color(35, 9, 3)
        self.document.set_font('NotoSans', 'B', font_size)
        self.document.multi_cell(0, 7, title)
        self.document.ln()

    def add_section_body(self, body, font_size):
        self.document.set_text_color(101, 98, 86)
        self.document.set_font('NotoSans', 'M', font_size)
        self.document.multi_cell(0, 5, unescape(body))
        self.document.ln()

    def add_section_source(self, source):
        self.document.set_text_color(158, 188, 159)
        self.document.set_font('NotoSans', 'LI', 12)
        self.document.multi_cell(0, 5, 'Source: ' + source)
        self.document.ln()

    def add_section_url(self, url):
        self.document.set_text_color(211, 184, 140)
        self.document.set_font('NotoSans', 'CI', 14)
        self.document.multi_cell(0, 5, url)
