#! /usr/bin/env python3
"""
This Is An Example Program For Learning Python
"""

if __name__ == "__main__":
    #
    # create list variables
    #
    T1 = ()  # Empty tuple
    T2 = (1, 2, 3, 7, 100, 20)
    print(type(T1), T1)
    print(type(T2), T2)

    #
    # operations
    #
    print(T2[3])
    print(T2[3:])
    print(T2[:3])
    print(T2 + T2)
    print(T2 * 3)
    print(len(T2))
    print(1 in T2)
    print(1 not in T2)
