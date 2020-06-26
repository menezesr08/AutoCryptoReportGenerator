import smtplib
import ssl
import configparser
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders


class EmailSender:

    def __init__(self, receiver_email):
        self.sender_email = "cryptoreportgen5@gmail.com"
        self.receiver_email = receiver_email
        self.port = 465
        self.context = ssl.create_default_context()
        self.message = MIMEMultipart("alternative")

    def send_email(self):
        self.create_message()
        self.attach_pdf()
        password = self.get_email_password()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.sender_email, password)
            server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())

    def create_message(self):
        self.message["Subject"] = "Your crypto report"
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email
        text = """\
        Hi,
        Please see the attached pdf to view your report.
        Thanks!"""
        self.message.attach(MIMEText(text, "plain"))

    def attach_pdf(self):
        filename = "main/pdfs/report.pdf"

        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        self.message.attach(part)

    @staticmethod
    def get_email_password():
        config = configparser.ConfigParser()
        config.read('main/config.ini')
        return config['EMAIL']['PASSWORD']


