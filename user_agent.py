import requests,logging

class UserAgent:

    def __init__(self):
        self.url = "https://www.whatsmyua.info/api/v1/ua?"

    def get_user_agent(self):
        logging.info("Getting User-Agent...")
        response = requests.get(self.url).json()
        ua = response[0].get("ua").get("rawUa")
        logging.info(f"User-Agent: {ua}")
        return ua