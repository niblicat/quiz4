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

def main():
    myPost = BlogPost(3312, "Servals are good", "servals can jump very high", 
                      ["cat", "animal", "informative"])

if __name__ == "__main__":
    main()