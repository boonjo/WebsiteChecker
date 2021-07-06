import requests
import time

class SendRequest:
    def __init__(self):
        self.makingList = MakeList()
        self.URL_list = None

    def receive_url_list(self):
        self.URL_list = self.makingList.get_list()

    def get_error_url(self, url_list):
        self.receive_url_list()
        error_url_list = []
        for url in url_list:
            try:
                status_code = requests.get(url).status_code
            except:
                time.sleep(5)
                error_url_list.append(url)
                continue
            if 400 <= status_code:
                error_url_list.append(url)
        return error_url_list