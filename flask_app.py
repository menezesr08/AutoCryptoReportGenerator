from flask import Flask, render_template, redirect, request, url_for
from celery import Celery
import RunReportScript
from threading import Thread

app = Flask(__name__)


# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
#
# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def get_options():
    currency = request.form.get('currency')
    time_period = request.form.get('period')
    email = request.form.get('email')
    thr = Thread(target=my_background_task, args=[currency, time_period, email])
    thr.start()
    return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template('success.html')


def my_background_task(currency, chosen_date, receiver_email):
    with app.app_context():
        RunReportScript.run(currency, chosen_date, receiver_email)


# @celery.task(name='run.my_background_task')
# def my_background_task(currency, chosen_date, receiver_email):
#     RunReportScript.run(currency, chosen_date, receiver_email)


if __name__ == '__main__':
    app.run(debug=True)
