import logging
from scraper import Scraper
from page_handler import PageHandler
from mail.mail_builder import MailBuilder
from mail.mail_sender import MailSender
from error_handler import PriceNotFoundError

logging.basicConfig(filename="log.txt",
                level=logging.DEBUG,
                format='%(levelname)s: %(asctime)s %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S')

def main():
    url = input("Website URL: ")

    logging.info("========= PriceTracker =========")
    scraper = Scraper(url)
    page_content = scraper.getPageContent()

    pageHandler = PageHandler(url, page_content)
    price_value = pageHandler.getPriceValueFromPageContent()

    mailBuilder = MailBuilder(page_content, price_value, url)

    if price_value is None:
        logging.info("Building error mail...")
        mail = mailBuilder.build_error_mail()
    else:
        logging.info("Building price mail...")
        logging.info(f"Price value is: {price_value.text.strip()}")
        mail = mailBuilder.build_mail()

    mailSender = MailSender(mail)
    mailSender.send_mail()

if __name__ == "__main__":
    main()