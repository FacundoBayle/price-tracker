import json
from email.message import EmailMessage

class MailBuilder:

    def __init__(self, page_content, price_value):
        self.page_content = page_content
        self.price_value = price_value
        with open('./credentials.json') as cred:
            credentials = json.load(cred)
            self.email_address = credentials["user"]
        with open('./mail/mail.html') as mailContent:
            self.mail_content = mailContent.read()

    def build_mail(self):
        print("Building Mail")

        msg = EmailMessage()
        msg['Subject'] = 'PriceTracker'
        msg['From'] = self.email_address
        msg['To'] = self.email_address

        mail = self.mail_content.format(price_value=self.price_value)
        msg.add_alternative(mail, subtype='html')

        return msg