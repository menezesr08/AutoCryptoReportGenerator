from flask import Flask, render_template, redirect, request, url_for
import run_report_script
from background_task import create_report_task
from worker import conn
from rq import Queue
import os

app = Flask(__name__)

que = Queue(connection=conn)


@app.route('/')
def index():
    return render_template('index.html')


@app.after_request
def add_security_headers(resp):
    resp.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return resp


@app.route('/', methods=['POST'])
def get_options():
    currency = request.form.get('currency')
    time_period = request.form.get('period')
    email = request.form.get('email')
    que.enqueue(create_report_task, currency, time_period, email)

    return redirect(url_for('success'))


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
