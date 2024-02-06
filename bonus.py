def RawLengthOfString(input):
    ...
def RawLengthOfInteger(input):
    ...
def RawLength(input):
    if (isinstance(input, list)):
        RawLengthOfListItems(input)
    else:
        print("not a list")

def RawLengthOfListItems(input):
    if (isinstance(input, list)):
        if (all(isinstance(item, str) for item in input)):
            print("string list")
        elif (all(isinstance(item, int) for item in input)):
            print("int list")
        else:
            print("list not accepted")
        for item in input:
            if (item)
    else:
        print("not a list")

def main():
    RawLength(["rawn", "32", "cowsss"])
    RawLength([711, 32, 15])
    RawLength([711, 32, "cows"])
    RawLength("ttt")

if (__name__ == "__main__"):
    main()