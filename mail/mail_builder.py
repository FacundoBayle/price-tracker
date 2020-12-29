import json, logging
from email.message import EmailMessage

class MailBuilder:

    def __init__(self, page_content, price_value, url):
        self.page_content = page_content
        self.price_value = price_value
        self.url = url

        with open('./mail/mail.html') as mailContent:
            self.mail_content = mailContent.read()
        with open('./mail/error-mail.html') as errorMailContent:
            self.error_mail_content = errorMailContent.read()

    def build_mail(self):
        msg = EmailMessage()
        msg['Subject'] = 'PriceTracker'
       
        mail = self.mail_content.format(price_value=self.price_value.text, url=self.url)
        msg.add_alternative(mail, subtype='html')

        logging.info("Price mail builded successfully.")
        return msg

    def build_error_mail(self):
        msg = EmailMessage()
        msg['Subject'] = '[ERROR] PriceTracker'

        mail = self.error_mail_content.format(url=self.url)
        msg.add_alternative(mail, subtype='html')

        logging.info("Error mail builded successfully.")
        return msg