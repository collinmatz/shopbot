class LinkCollection:
    def __init__(self):
        self.collection = []
    
    def addLink(self, link):
        self.collection.append(link)

    def printLinks(self):
        if len(self.collection) == 0:
            print("Currently tracking 0 links")
        for i in range(len(self.collection)):
            print((i + 1), ")", self.collection[i].getUrl())