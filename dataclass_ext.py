from dataclasses import dataclass
from datetime import datetime

@dataclass
class BlogPost:
    userID: int
    title: str
    content: str
    tags: list[str]
    initialCreation: datetime = datetime.now()
    lastModified: datetime = initialCreation

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

if __name__ == "__main__":
    main()