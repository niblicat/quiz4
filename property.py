from datetime import datetime

class BlogPost:
    def __init__(self, userID, title, content, tags):
        self.userID: int = userID
        self._title: str = title
        self._content: str = content
        self._tags: list[str]= tags
        self._initialCreation: datetime = datetime.now()
        self._lastModified: datetime = self._initialCreation
    
    @property
    def content(self):
        return self._content
    
    # used to edit content
    @content.setter
    def content(self, newContent):
        self._content = newContent
        self._lastModified = datetime.now()

    @property
    def title(self):
        return self._title
    
    # used to edit title
    @title.setter
    def title(self, newtitle):
        self._title = newtitle
        self._lastModified = datetime.now()

    @property
    def tags(self):
        return self._tags
    
    # used to edit tags
    @tags.setter
    def tags(self, newtags):
        self._tags = newtags
        self._lastModified = datetime.now()

    def __str__(self) -> str:
        tagList: str = "["
        for tag in self._tags:
            tagList += "\"" + tag + "\","
        if (len(tagList) > 0):
            tagList = tagList[:-1]
        tagList += "]"
        
        lastModified = self._lastModified.strftime("%d/%m/%Y, %H:%M:%S")
        initialCreation = self._initialCreation.strftime("%d/%m/%Y, %H:%M:%S")
        
        return "" + str(self.userID) + ":\"" + self._title + "\"-\"" + self._content + "\"-" + tagList + "-" + lastModified + "-" + initialCreation

def main():
    myPost = BlogPost(3312, "Servals are good", "servals can jump very high", 
                      ["cat", "animal", "informative"])
    print(myPost.__str__())
    myPost.content = input("type a new message:")
    print(myPost.__str__())

if __name__ == "__main__":
    main()