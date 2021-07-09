import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import requests


SITE_LIST = os.environ["SITE_LIST"]              # Name of the file that contains a list of URLs
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]  # Token from Slack 
CHANNEL = os.environ["CHANNEL"]                  # Slack Channel ID

class readFile:
    """
        Reads the SITE_LIST file that contains the URLs
    """
    
    def readURL(self):
        """
            Takes the SITE_LIST file and reads the URLs by line

            Returns: List of URLs
        """
        f = open(SITE_LIST, 'r')
        URL_list = []
        lines = f.readlines()

        for line in lines:
            URL_list.append(line.strip())

        f.close()

        return URL_list

class URLChecker:
    """
        Takes the list of URLs and checks if any sites are dead
    """
    def __init__(self):
        self.makingList = readFile()
        self.URL_list = None

    def receive_url_list(self):
        self.URL_list = self.makingList.readURL()

    def get_error_url(self):
        """
            Given the list of URLs, checks the status for each one
            
            If there are dead sites, then returns a list of error messages of the dead sites; 
            else return none
        """
        self.receive_url_list()
        error_msg_list = []
        
        for url in self.URL_list:
            try:
                r = requests.get(url)
                r.raise_for_status()
            except requests.exceptions.RequestException as err:
                error_msg_list.append(err)
                
        return error_msg_list

def listToString(list):
    """ 
        Function to convert a list to a string
        
        Returns a fromatted string of list components
    """
    
    # initialize an empty string
    strlist = "\n\n" 
     
    return (strlist.join("💀 " + str(site) for site in list))

def main():
    # Token can be found in OAuth & Permissions -> OAuth Tokens for Your Workspace
    # Make sure to allow chat:write for the Bot Token to enable writing messages    
    client = WebClient(token=SLACK_BOT_TOKEN)

    # Checking if all sites are alive
    websiteChecker = URLChecker()
    errorlist = websiteChecker.get_error_url()

    # if length > 0, that means at least one site is dead from the list
    if len(errorlist) != 0:
        try:        
            # Leave a message in the appropriate channel
            response = client.chat_postMessage(
                channel=CHANNEL,
                text="🚨 There are " + str(len(errorlist)) + " site(s) that are dead 🚨: \n\n "+ listToString(errorlist)
            )
        except SlackApiError as e:    
            assert e.response["error"] 
