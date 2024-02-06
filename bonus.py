def RawLengthOfString(input: str) -> int:
    """Returns the number of characters from a string"""
    return len(input)

def RawLengthOfInteger(input: int) -> int:
    """Returns the number of characters from an integer"""
    output = 1
    mult = 10
    while (input > mult):
        mult *= 10
        output += 1
    return output

def RawLengthOfListItems(input: list[str | int]) -> list[int]:
    """Returns the number of characters from a list of strings/integers"""
    result = []
    for item in input:
        if (isinstance(item, str)):
            itemOutput = RawLengthOfString(item)
        elif (isinstance(item, int)):
            itemOutput = RawLengthOfInteger(item)
        else:
            print("type of " + str(type(item)) + " not accepted")
            itemOutput = None
        result.append(itemOutput)
    return result

def RawLength(input: int | str | list[str | int]) -> int | list[int]:
    """Returns the number of characters from a string, an integer, or a list of strings/integers"""
    if (isinstance(input, list)):
        return RawLengthOfListItems(input)
    elif (isinstance(input, str)):
        return RawLengthOfString(input)
    elif (isinstance(input, int)):
        return RawLengthOfInteger(input)
    else:
        print("type of " + str(type(input)) + " not accepted")
        return None


def main():
    print(RawLength(["rawn", "32", "cowsss"]))
    print(RawLength([711, 32, 15]))
    print(RawLength([711, 32, "cows"]))
    print(RawLength([12, 3.5]))
    print(RawLength("ttt"))
    print(RawLength(3.5))

if (__name__ == "__main__"):
    main()