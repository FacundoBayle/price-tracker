import requests
from bs4 import BeautifulSoup
from user_agent import UserAgent

class Scraper:

    def __init__(self, url):
        self.url = url

    def getPageContent(self):
        ua = UserAgent().get_user_agent()
        headers_obj = {
            "User-Agent": ua
        }
        
        page = requests.get(self.url, headers=headers_obj)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

