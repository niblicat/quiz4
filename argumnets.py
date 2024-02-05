# named "argumnets.py" as described by project requirements
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(help="enter a string",dest="myString",type=str)
    ap.add_argument(help="enter an integer",dest="myInt",type=int)
    ap.add_argument(help="enter a real number",dest="myFloat",type=float)

    args = ap.parse_args()

    myString = args.myString
    myInt = args.myInt
    myFloat = args.myFloat

    print(myString,myInt,myFloat)


if (__name__ == "__main__"):
    main()