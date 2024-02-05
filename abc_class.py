from abc import ABC, abstractmethod

# Cats can walk and vocalise
class Cat(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def Vocalise():
        ...
    @abstractmethod
    def Walk():
        ...

# A domestic cat is a standard cat you may find in a household
class DomesticCat(Cat):
    def Vocalise(self):
        print("meow")
    def Walk(self):
        print(self.name, "the cat walked 0.9 metres in one second")

# A serval is a wild cat that originates from Africa
class Serval(Cat):
    def Vocalise(self):
        print("waow")
    def Walk(self):
        print(self.name, "the serval walked 1.0 metres in one second")

def main():
    myCat = DomesticCat("mittens")
    myCat.Vocalise()
    myCat.Walk()
    myServal = Serval("sogga")
    myServal.Vocalise()
    myServal.Walk()

if (__name__ == "__main__"):
    main()