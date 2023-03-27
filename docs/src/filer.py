#!/usr/bin/env python3


if __name__ == "__main__":
    #    try:
    f = open("LICENSE.txt")
    lines = f.readlines()
    f.close()
    # except:
    #    print("Failed")

    for x in lines:
        print(x)

    #
    # Shorter version
    #
    for line in open("LICENSE.txt"):
        print(line)
