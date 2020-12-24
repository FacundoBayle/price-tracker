class MailSender:

    def __init__(self, mail):
        self.mail = mail

    def send_mail(self):
        print("Sending Mail")

    def has_to_send_mail(self):
        return False