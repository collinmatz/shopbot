class LinkCollection:
    def __init__(self):
        self.collection = []
        self.size = 0
    
    def addLink(self, link):
        self.collection.append(link)
        self.size += 1

    def deleteLink(self, url):
        for link in range(len(self.collection)):
            if (self.collection[link].getUrl() == url):
                del self.collection[link]
                self.size -= 1
                return True
            else:
                return False

    def printLinks(self):
        if len(self.collection) == 0:
            print("Currently tracking 0 links")
        for i in range(len(self.collection)):
            print((i + 1), ")", self.collection[i].getTitle())

    def getLink(self, url):
        for link in self.collection:
            if (link.getUrl() == url):
                return link
            else:
                return None