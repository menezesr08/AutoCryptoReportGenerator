import pickle

import pandas as pd

import matplotlib.dates as mdates

from datetime import datetime

from fpdf import FPDF, HTMLMixin
from matplotlib.ticker import FuncFormatter

import Helper



import matplotlib.pyplot as plt


from enums.Limits import Limits

import fpdf
import os

from main.ReportGenerator import ReportGenerator

report: ReportGenerator = ReportGenerator("BTC", chosen_date="month")
data = report.news
from jinja2 import Template

from jinja2 import Environment, FileSystemLoader

fpdf.set_global("SYSTEM_TTFONTS", 'C:\\Users\\menez\\PycharmProjects\\Stock_Notifier\\fonts')

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
document.add_font("NotoSans", style="B", fname="NotoSans-Bold.ttf", uni=True)
document.add_font("NotoSans", style="I", fname="NotoSans-Italic.ttf", uni=True)
document.add_font("NotoSans", style="BI", fname="NotoSans-BoldItalic.ttf", uni=True)
document.add_font("NotoSans", style="M", fname="NotoSans-Medium.ttf", uni=True)
document.add_font("NotoSans", style="TI", fname="NotoSans-ThinItalic.ttf", uni=True)
document.add_font("NotoSans", style="CI", fname="NotoSans-ExtraCondensedItalic.ttf", uni=True)
document.add_font("NotoSans", style="LI", fname="NotoSans-LightItalic.ttf", uni=True)


document.set_font('NotoSans', 'B', 20)
document.set_text_color(57, 62, 65)
document.add_page()
document.multi_cell(0, 5, 'News', align='C')
document.ln()
document.ln()

for article in data:
    document.set_text_color(35, 9, 3)
    document.set_font('NotoSans', 'B', 16)
    document.multi_cell(0, 7, article['title'])
    document.ln()
    document.set_text_color(101, 98, 86)
    document.set_font('NotoSans', 'M', 14)
    document.multi_cell(0, 5, article['body'])
    document.ln()
    document.set_text_color(158, 188, 159)
    document.set_font('NotoSans', 'LI', 12)
    document.multi_cell(0, 5, 'Source: ' + article['source'])
    document.ln()
    document.set_text_color(211, 184, 140)
    document.set_font('NotoSans', 'CI', 14)
    document.multi_cell(0, 5, article['url'])
    document.ln()
    document.ln()

document.output('report.pdf')
