#!/usr/bin/env python3


if __name__ == "__main__":

    try:
        f = open("example2.txt", "w")
    except:
        print("Failed to open for write")

    print("HELLO to a file!", file=f)
    f.close()
