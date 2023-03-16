#! /usr/bin/env python3

"""
This Is An Example Program For Learning Python
"""

if __name__ == "__main__":
    #
    # create list variables
    #
    L1 = []  # Empty list
    L2 = [1, 2, 3, 7, 100, 20]
    print(type(L1), L1)
    print(type(L2), L2)

    #
    # operations
    #
    print(L2[3])
    L2[3] = 400
    print(L2[3])
    print(L2[3:])
    print(L2[:3])
    print(L2 + L2)
    print(L2 * 3)
    print(len(L2))
    print(1 in L2)
    print(1 not in L2)

    #
    # Methods
    #
    L2.append(99)
    print(L2)
    L2.extend([21, 22, 23])
    print(L2)
    L2.insert(4, 10000)
    print(L2)
    L2.pop()
    print(L2)
    L2.sort()
    print(L2)
