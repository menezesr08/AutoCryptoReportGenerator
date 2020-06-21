import yagmail

receiver = "menezesr08@gmail.com"
body = "Hello there from Yagmail"
filename = "main/pdfs/report.pdf"

yag = yagmail.SMTP("cryptoreportgen5@gmail.com", password="Lightus12345")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body,
    attachments=filename,
)
