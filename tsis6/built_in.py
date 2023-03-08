import numpy
import time
import math


def mult(my_list):
    res = numpy.prod(my_list)
    return res


def cnt(my_str):
    upper = 0
    lower = 0
    for i in my_str:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    return upper, lower


def is_palindrome(my_str):
    my_str = my_str.casefold()
    rev_str = reversed(my_str)

    if list(my_str) == list(rev_str):
        return True
    else:
        return False


def inv_root(num, sec):
    print("start")
    time.sleep(sec/1000)
    root = math.sqrt(num)
    print(f"Square root of {num} is {root} after {sec} milliseconds")


def true_tuple(my_tuple):
    res = all(my_tuple)
    return res



