import argparse
from scraper import Scraper
from page_handler import PageHandler

def main():
    url = input("Website URL: ")
    #user_agent = input("User-Agent: ")

    #scraper = Scraper(url, user_agent)
    #page_content = scraper.getPageContent()

    pageHandler = PageHandler(url)
    pageHandler.handlePageContent()

if __name__ == "__main__":
    main()