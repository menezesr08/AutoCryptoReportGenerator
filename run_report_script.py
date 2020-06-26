from main.report_generator import ReportGenerator


def run(currency, chosen_date, receiver_email):
    report = ReportGenerator(currency, chosen_date, receiver_email)
    report.generate_report()


