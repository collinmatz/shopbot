# defines the link class
# each link stores a url to a website that is currently being tracked
#   by the user

import requests
from bs4 import BeautifulSoup

class Link:
    def __init__(self, url, title, pref=0):
        self.url = url
        self.title = title
        self.pref = pref

    def getUrl(self):
        return self.url

    def getTitle(self):
        return self.title

    def setUrl(self, newUrl):
        if newUrl == self.url:
            return False
        else:
            try: 
                response = requests.get(newUrl) # returns true if the url is okay
            except:
                print("Error setting URL. Check that you input the correct URL")
            else:
                self.url = newUrl
                print("URL Set as", self.url)
                return self.url

    def getContent(self):
        request = requests.get(self.url)
        print(request)