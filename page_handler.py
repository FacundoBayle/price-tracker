import sys,logging
from error_handler import InvalidPageError

class PageHandler:
    
    def __init__(self, url, page_content):
        self.url = url
        self.page_content = page_content
        self.PAGES_TRACK_ID = {
            'mercadolibre': "price-tag",
            'tiendamia': "currency_price",
        }

    def getPageFromUrl(self):
        for page in self.PAGES_TRACK_ID:
            if page in self.url:
                return page

    def getPriceIdToTrack(self, page_name):
        return self.PAGES_TRACK_ID[page_name]

    def getPriceValueFromPageContent(self):
        page_name = self.getPageFromUrl()

        if page_name is None:
            logging.error(f"Invalid Page for url: {self.url}. The website is not in the list of sites available to track.")
            raise InvalidPageError
        else:
            logging.info(f"Page: {page_name}")

        price_id = self.getPriceIdToTrack(page_name)
        
        return self.page_content.find("span", class_=price_id)
        

