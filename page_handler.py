import sys

class PageHandler:
    
    def __init__(self, url, page_content):
        self.url = url
        self.PAGES_TRACK_ID = {
            'mercadolibre': "price-tag",
            'tiendamia': "currency_price",
        }
        self.page_content = page_content

    def getPageFromUrl(self):
        for page in self.PAGES_TRACK_ID:
            if page in self.url:
                return page

    def getPriceIdToTrack(self, page_name):
        return self.PAGES_TRACK_ID[page_name]

    def getPriceValueFromPageContent(self):
        page_name = self.getPageFromUrl()

        if page_name is None:
            sys.exit("PAGE NOT FOUND, STOP EXECUTION") # change for error_handler
        else:
            print(page_name)

        price_id = self.getPriceIdToTrack(page_name)
        print(price_id)

        return self.page_content.find("span", class_=price_id).text
        

