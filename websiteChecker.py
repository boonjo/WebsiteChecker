import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from URLChecker import URLChecker

def listToString(list):
    """ Funciton to convert a list to a string
    """
    
    # initialize an empty string
    strlist = " \n" 
    
    return (strlist.join(list))

# Token can be found in OAuth & Permissions -> OAuth Tokens for Your Workspace
# Make sure to allow chat:write for the Bot Token to enable writing messages
SLACK_BOT_TOKEN="xoxb-2256225158097-2240634984229-X6j1Tbpt1s20Bz0EXeqCnLWO"
slack_token = os.environ.get(SLACK_BOT_TOKEN)
client = WebClient(token=SLACK_BOT_TOKEN)

# Checking if all sites are alive
websiteChecker = URLChecker()
errorlist = websiteChecker.get_error_url()

# if length > 0, that means at least one site is dead from the list
if len(errorlist) != 0:
    try:
        # Leave a message in the appropriate channel
        response = client.chat_postMessage(
            channel="C027BNN46GL",
            text="There are " + str(len(errorlist)) + " site(s) that are dead: \n "+ listToString(errorlist)
        )
    except SlackApiError as e:    
        assert e.response["error"] 