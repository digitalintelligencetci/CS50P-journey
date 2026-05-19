#!/usr/bin/env python3


def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return s


def main():
    hello_user = input("How are you feeling? ")
    result = convert(hello_user)
    print(result)


main()
