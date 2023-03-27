#!/usr/bin/env python3


if __name__ == "__main__":
    try:
        f = open("example.txt", "w")
    except:
        print("Failed to open for write")
    f.write("Put this string in the file\n")
    f.writelines(["String 1\n", "String 2\n"])
    f.flush()
    f.close()
