#! /usr/bin/env python3


def factorial(n=1):
    """
    This is the function's comment, it explains
    what the function does, how it does it and why it
    does it
    """
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    # Single line comment example!
    print(factorial(5))
