#! /usr/bin/env python3
"""
This Is An Example Program For Learning Python
"""

if __name__ == "__main__":
    #
    # create dictionary variables
    #
    D1 = {}  # Empty dictionary
    D2 = {"One": 1, "Two": 2, "Three": 3}
    print(type(D1), D1)
    print(type(D2), D2)

    #
    # Operations and methods
    #
    print(len(D2))
    print(D2["One"])
    D2["One"] = [1, 2, 3, 4]
    print(D2)
    print("One" in D2)
    print("No" in D2)
    print(D2.keys())
    print(D2.values())
    print(D2.items())
