from datetime import datetime

class BlogPost:
    def __init__(self, userID, title, content, tags):
        self.userID: int = userID
        self.title: str = title
        self.content: str = content
        self.tags: list[str]= tags
        self.initialCreation: datetime = datetime.now()
        self.lastModified: datetime = self.initialCreation
    
    def GetContent(self) -> str:
        return self.content
    
    def SetContent(self, newContent):
        self.content = newContent
        self.lastModified = datetime.now()

    def GetTitle(self) -> str:
        return self.title
    
    def SetTitle(self, newtitle):
        self.title = newtitle
        self.lastModified = datetime.now()

    def GetTags(self) -> list[str]:
        return self.tags
    
    def SetTags(self, newtags):
        self.tags = newtags
        self.lastModified = datetime.now()

    def __str__(self) -> str:
        tagList: str = "["
        for tag in self.tags:
            tagList += "\"" + tag + "\","
        if (len(tagList) > 0):
            tagList = tagList[:-1]
        tagList += "]"
        
        lastModifiedString = self.lastModified.strftime("%d/%m/%Y, %H:%M:%S")
        initialCreationString = self.initialCreation.strftime("%d/%m/%Y, %H:%M:%S")
        
        return "" + str(self.userID) + ":\"" + self.title + "\"-\"" + self.content + "\"-" + tagList + "-" + lastModifiedString + "-" + initialCreationString

def main():
    myPost = BlogPost(3312, "Servals are good", "servals can jump very high", 
                      ["cat", "animal", "informative"])
    print(myPost.__str__())
    myPost.SetContent(input("type a new message:"))
    print(myPost.__str__())

if __name__ == "__main__":
    main()