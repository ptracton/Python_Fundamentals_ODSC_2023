#! /usr/bin/env python3

if __name__ == "__main__":
    languages = ["python", "java", "c", "lisp", "perl"]
    count = 0
    while count < len(languages):
        print(languages[count])
        count += 1
    count = 0
    while count in range(10):
        print(count)
        count += 1
    else:
        print("Done")
    count = 0
    while count in range(10):
        print(count)
        count += 1
        if count > 4:
            break
    else:
        print("Done")
