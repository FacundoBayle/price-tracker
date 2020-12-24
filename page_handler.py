class PageHandler:
    
    def __init__(self, url):
        self.url = url
        self.PAGES = ["mercadolibre", "tiendamia"] 

    def getPageFromUrl(self):
        for page in self.PAGES:
            if page in self.url:
                return page

    def handlePageContent(self):
        page_name = self.getPageFromUrl()

        if page_name is None:
            print("PAGE NOT FOUND")
        else:
            print(page_name)
