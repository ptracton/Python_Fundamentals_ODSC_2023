#! /usr/binenv python3

"""
This Is An Example Program For Learning Python
"""


def function_example(param1="Hi", param2=False):
    """
    This is the function's doc string,
    it is a comment that explains the
    function and how to use it.

    This function takes 2 parameters (param 1 and param2)
    and prints them out.

    EX: function_example("1", "One")
    """
    print(param1, param2)
    return


if __name__ == "__main__":
    function_example()
    function_example("1", "One")
    function_example(param2="there!")
    function_example(param2="order", param1="Reverse")
    function_example(param1=2)
