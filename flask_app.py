from flask import Flask, render_template, redirect, request, url_for
import run_report_script
from threading import Thread
from flask import Flask
from celery import Celery

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def get_options():
    currency = request.form.get('currency')
    time_period = request.form.get('period')
    email = request.form.get('email')
    my_background_task(currency, time_period, email)
    return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template('success.html')


def my_background_task(currency, chosen_date, receiver_email):
    run_report_script.run(currency, chosen_date, receiver_email)


if __name__ == '__main__':
    app.run(debug=True)
