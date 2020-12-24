import sys
from scraper import Scraper
from page_handler import PageHandler
from mail.mail_builder import MailBuilder
from mail.mail_sender import MailSender
from error_handler import PriceNotFoundError

def main():
    url = input("Website URL: ")

    scraper = Scraper(url)
    page_content = scraper.getPageContent()

    pageHandler = PageHandler(url, page_content)
    price_value = pageHandler.getPriceValueFromPageContent()

    print(price_value.text)

    if price_value is None:
        raise PriceNotFoundError
        #send error mail

    mailBuilder = MailBuilder(page_content, price_value.text)
    mail = mailBuilder.build_mail()
    
    mailSender = MailSender(mail)
    mailSender.send_mail()

if __name__ == "__main__":
    main()