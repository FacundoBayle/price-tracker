import argparse
from scraper import Scraper
from page_handler import PageHandler

def main():
    url = input("Website URL: ")

    scraper = Scraper(url)
    page_content = scraper.getPageContent()

    pageHandler = PageHandler(url, page_content)
    price_value = pageHandler.getPriceValueFromPageContent()

    print("hola")
    print(price_value)

if __name__ == "__main__":
    main()