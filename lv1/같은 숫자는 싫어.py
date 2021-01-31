# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3

import numpy as np
import functools
from itertools import takewhile


def set_diff(arr):
    result = [arr[0]]

    def return_diff(reference, mutable_element):
        if reference != mutable_element:
            result.append(mutable_element)
            return mutable_element

        else:
            return reference

    functools.reduce(return_diff, arr)
    return result

if __name__ == '__main__':
    arr = [1,1,2,3,3,4,5,5,5,6,7,8,9, 2, 3,4,4,5,6,7,7,10]
    set_diff(arr)