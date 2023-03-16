#! /usr/bin/env python3

if __name__ == "__main__":
    languages = ["python", "java", "c", "lisp", "perl"]
    for x in languages:
        print(x)
    for x in range(10):
        print(x)
    else:
        print("Done")
    for x in range(10):
        print(x)
        if x > 4:
            break
    else:
        print("Done")
    my_dict = {1: "One", 2: "Two", 3: "Three"}
    for k, v in my_dict.items():
        print(k, v)
