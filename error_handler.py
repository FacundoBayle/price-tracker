class Error(Exception):
    pass

class InvalidPageError(Error):
     def __init__(self):
        error_message="The website is not in the list of sites available to track."
        super().__init__(error_message)
