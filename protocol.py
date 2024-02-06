from typing import Protocol

# Cats can walk and vocalise
class Cat(Protocol):
    def __init__(self, name):
        ...
    def Vocalise():
        ...
    def Walk():
        ...

# A domestic cat is a standard cat you may find in a household
class DomesticCat(Cat):
    def __init__(self, name):
        self.name = name
    def Vocalise(self):
        print("meow")
    def Walk(self):
        print(self.name, "the cat walked 0.9 metres in one second")

# A serval is a wild cat that originates from Africa
class Serval(Cat):
    def __init__(self, name):
        self.name = name
    def Vocalise(self):
        print("waow")
    def Walk(self):
        print(self.name, "the serval walked 1.0 metres in one second")

def main():
    myCat: Cat = DomesticCat("mittens")
    myCat.Vocalise()
    myCat.Walk()
    myServal: Cat = Serval("sogga")
    myServal.Vocalise()
    myServal.Walk()

if (__name__ == "__main__"):
    main()