#!/usr/bin/env python3


def key_trigger(key=None):
    d = {1: "One"}
    return d[key]


def trigger(x, y):
    return x / y


if __name__ == "__main__":

    try:
        print(key_trigger(1))
        print(key_trigger())  # KeyError
        print(trigger(1, 2))
        print(trigger(1, 0))  # ZeroDivisionError
    except ZeroDivisionError as e:
        print("Exception: %s" % (e.args))
    except KeyError:
        print("Key Error")
    else:
        print("All is well")
    finally:
        print("Finally")
