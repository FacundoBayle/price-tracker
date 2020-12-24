import requests
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self, url):
        self.url = url
        self.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

    def getPageContent(self):
        headers_obj = {
            "User-Agent": self.USER_AGENT
        }
        page = requests.get(self.url, headers=headers_obj)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

