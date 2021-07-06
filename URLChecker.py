import requests
import time
from URLReader import readFile

class URLChecker:
    def __init__(self):
        self.makingList = readFile()
        self.URL_list = None

    def receive_url_list(self):
        self.URL_list = self.makingList.readURL()

    def get_error_url(self):
        self.receive_url_list()
        error_url_list = []
        for url in self.URL_list:
            try:
                status_code = requests.get(url).status_code
            except:
                time.sleep(2)
                error_url_list.append(url)
                continue
            if 400 <= status_code:
                error_url_list.append(url)
        return error_url_list