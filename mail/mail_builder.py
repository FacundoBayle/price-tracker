class MailBuilder:

    def __init__(self, page_content, price_value):
        self.page_content = page_content
        self.price_value = price_value

    def build_mail(self):
        print("Building Mail")
        return ""