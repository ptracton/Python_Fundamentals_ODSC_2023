#! /usr/bin/env python3
"""
This Is An Example Program For Learning Python
"""

if __name__ == "__main__":
    x = bytearray([0x31, 0x32, 0x33])
    print(x)

    y = bytearray([4, 5, 5])
    print(y)

    print(x + y)
    print(x.count(0x32))
    print(y.count(5))
    print(x.decode("utf-8"))
    print(y.decode("utf-8"))
