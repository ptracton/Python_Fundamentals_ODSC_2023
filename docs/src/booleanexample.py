#! /usr/bin/env python3

"""
This Is An Example Program For Learning Python
"""

if __name__ == "__main__":
    #
    # create boolean variables
    #
    bool1_var = True
    bool2_var = False
    print(type(bool1_var))
    print(type(bool2_var))

    #
    # Some simple if logic and inversion
    #
    if bool1_var is True:
        bool1_var = not bool1_var
    print(bool1_var)

    if bool2_var is not True:
        print(bool2_var)
