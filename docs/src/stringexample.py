#! /usr/bin/env python3
"""
This Is An Example Program For Learning Python
"""

if __name__ == "__main__":
    #
    # create string variables
    #
    s1 = "String 1"
    s2 = "String 2"
    s3 = """String 3"""

    print(s1)
    print(s2)
    print(s3)

    #
    # Basic Operations
    #
    print(s1[4])
    print(s1[:4])
    print(s1[4:])
    print(s1 + s2)
    print(s1 * 3)
    print(len(s1))
    print("1" in s1)
    print("2" in s1)
    print("q" not in s1)

    #
    # Basic methods
    #
    print(s1.join(["more", "stuff", "added"]))
    print(s1.upper())
    print(s1.lower())
    print("This is a long string".split(" "))
    print("This is a long string".strip("T"))
