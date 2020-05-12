import pickle

import pandas as pd

import matplotlib.dates as mdates

from datetime import datetime

from fpdf import FPDF, HTMLMixin
from matplotlib.ticker import FuncFormatter

import Helper
from API import CryptoReport

import matplotlib.pyplot as plt

from ReportGenerator import ReportGenerator
from enums.Limits import Limits

import fpdf
import os

report: ReportGenerator = ReportGenerator("BTC", chosen_date="month")
data = report.news
print(data)
from jinja2 import Template

from jinja2 import Environment, FileSystemLoader


# news = report.news
# class MyFPDF(FPDF, HTMLMixin):
#     pass
#
#
# pdf = MyFPDF()
# pdf.add_page()
# pdf.set_font('Arial', 'B', 16)
#
# root = os.path.dirname(os.path.abspath(__file__))
# templates_dir = os.path.join(root, 'templates')
# env = Environment(loader=FileSystemLoader(templates_dir))
# template = env.get_template('grid.html')
#
# pdf.write_html(template.render())
# pdf.output('tuto1.pdf', 'F')

document = fpdf.FPDF()

document.set_font('Times', 'B', 20)
document.set_text_color(19, 83, 173)
document.add_page()
document.cell(0, 5, 'News')

for article in data:
    document.set_font('Times', '', 16)
    document.multi_cell(0, 5, article['title'])
    document.set_font('Times', '', 14)
    document.multi_cell(0, 5, article['body'])
    document.set_font('Times', '', 12)
    document.multi_cell(0, 5, article['source'])
    document.ln()
    document.ln()

document.output('report.pdf')
