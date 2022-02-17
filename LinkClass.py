# defines the link class
# each link stores a url to a website that is currently being tracked
#   by the user

import requests

class Link:
    def __init__(self, url):
        self.url = url

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        if newUrl == self.url:
            return("New URL matches old URL")
        else:
            try: 
                response = requests.get(newUrl) # returns true if the url is okay
            except:
                return("Error setting URL. Check that you input the correct URL")
            else:
                self.url = newUrl
                return("URL Set as", self.url)