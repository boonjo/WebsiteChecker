import requests
import time
from URLReader import readFile
from urllib3.exceptions import HTTPError as BaseHTTPError

class URLChecker:
    def __init__(self):
        self.makingList = readFile()
        self.URL_list = None

    def receive_url_list(self):
        self.URL_list = self.makingList.readURL()

    def get_error_url(self):
        self.receive_url_list()
        error_msg_list = []
        for url in self.URL_list:
            try:
                r = requests.get(url)
                r.raise_for_status()
            except requests.exceptions.RequestException as err:
                error_msg_list.append(err)
        return error_msg_list
