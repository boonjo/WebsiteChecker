import os

SITE_LIST = os.environ["SITE_LIST"]

class readFile:
    """Reads the file URLlist.txt and returns a list of URLs"""
    
    def readURL(self):
        f = open(SITE_LIST, 'r')

        URL_list = []

        lines = f.readlines()

        for line in lines:
            URL_list.append(line.strip())


        f.close()

        return URL_list