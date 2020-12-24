import argparse
from scraper import Scraper

def main():
    url = input("Website URL: ")
    user_agent = input("User-Agent: ")

    scraper = Scraper(url, user_agent)
    page_content = scraper.getPageContent()

if __name__ == "__main__":
    main()