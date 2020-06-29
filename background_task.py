import run_report_script


def create_report_task(currency, chosen_date, receiver_email):
    run_report_script.run(currency, chosen_date, receiver_email)
