import requests
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self, url, headers):
        self.url=url
        self.headers=headers

    def getPageContent(self):
        headers_obj = {
            "User-Agent": self.headers
        }
        page = requests.get(self.url, headers=headers_obj)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

