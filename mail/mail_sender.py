import json,smtplib,logging

class MailSender:

    def __init__(self, mail):
        self.mail = mail
        with open('./credentials.json') as f:
            credentials = json.load(f)
            self.email_address = credentials["user"]
            self.email_password = credentials["password"]

    def send_mail(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email_address, self.email_password)
            
            logging.info("Sending Mail")
            
            smtp.send_message(self.mail)
        
    def has_to_send_mail(self):
        return False